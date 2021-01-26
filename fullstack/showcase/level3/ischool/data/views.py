from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django import forms
from django.forms import ValidationError

from .models import User, Course, Division, Student
from .filters import CourseFilter, DivisionFilter, StudentFilter
import json
# rest framework view imports
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import generics, filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import CourseSerializer, DivisionSerializer, StudentSerializer

# authentications
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "data/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "data/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "data/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "data/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "data/register.html")


def index(request):
    if request.method == "GET":
        try:
            courses = Course.objects.all()
        except Course.DoesNotExist:
            return render(request, 'data/index.html', {
                "message": "does not exist",
            })

        return render(request, 'data/index.html', {
            "course": courses,
        })


@login_required
def division(request, id):
    if request.method == "GET":
        try:
            c = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return render(request, 'data/division.html', {
                "message": "course does not exist",
            })

        try:
            d = Division.objects.filter(course=c)
        except Division.DoesNotExist:
            return render(request, 'data/division.html', {
                "message": "course does not exist",
            })

        division = DivisionFilter(request.GET, queryset=Division.objects.filter(course=c))

        return render(request, 'data/division.html', {
                "course": c,
                "division": d,
                "filter": division
            })
    else:
        return render(request, 'data/division.html', {
                "message": "Only GET allowed",
            })


@login_required
def student(request, id):
    if request.method == "GET":
        try:
            d = Division.objects.get(id=id)
        except Division.DoesNotExist:
            return render(request, 'data/student.html', {
                "message": "division does not exist",
            })

        try:
            s = Student.objects.filter(division=d)
        except Student.DoesNotExist:
            return render(request, 'data/student.html', {
                "message": "division does not exist",
            })

        student = StudentFilter(request.GET, queryset=Student.objects.filter(division=d))

        return render(request, 'data/student.html', {
                "division": d,
                "student": s,
                "filter": student
            })
    else:
        return render(request, 'data/student.html', {
                "message": "Only GET allowed",
            })


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title']

    def post(self, request):
        # title = request.POST["title"]
        # c = Course.objects.create(title=title)
        # c.save()
        # return Response({"message:created new course."},
        #                 status=status.HTTP_201_CREATED)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.error,
                        status=status.HTTP_400_BAD_REQUEST)


class CourseAPIView(APIView):
    """
    api end point to create a GET, PUT and DELETE request
    """
    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        try:
            data = self.get_object(id)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(data)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)

    def put(self, request, id):
        data = self.get_object(id)
        serializer = CourseSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.error,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            data = self.get_object(id)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        operation = data.delete()
        response = {}
        if operation:
            response["success"] = "deleted successfully."
        else:
            response["failure"] = "deletion failed."
        return Response(data=response)


class DivisionList(generics.ListAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'room', 'course']
    search_fields = ['title', 'room']
    ordering_fields = ['title']

    def post(self, request):
        serializer = DivisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.error,
                        status=status.HTTP_400_BAD_REQUEST)


class DivisionAPIView(APIView):
    """
    api end point to create a GET, PUT and DELETE request
    """
    def get_object(self, id):
        try:
            return Division.objects.get(id=id)
        except Division.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        data = self.get_object(id)

        serializer = DivisionSerializer(data)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)

    def put(self, request, id):
        data = self.get_object(id)
        serializer = DivisionSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.error,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        data = self.get_object(id)
        operation = data.delete()
        response = {}
        if operation:
            response["success"] = "deleted successfully."
        else:
            response["failure"] = "deletion failed."
        return Response(data=response)


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'surname', 'division']
    search_fields = ['name', 'surname', 'grade']
    ordering_fields = ['name']

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.error,
                        status=status.HTTP_400_BAD_REQUEST)


class StudentAPIView(APIView):
    """
    api end point to create a GET, PUT and DELETE request
    """
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        try:
            data = self.get_object(id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(data)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)

    def put(self, request, id):
        data = self.get_object(id)
        serializer = StudentSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.error,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            data = self.get_object(id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        operation = data.delete()
        response = {}
        if operation:
            response["success"] = "deleted successfully."
        else:
            response["failure"] = "deletion failed."
        return Response(data=response)
