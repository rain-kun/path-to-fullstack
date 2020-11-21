from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django import forms

from django.http import JsonResponse
import json

from .models import User, Post, Like


class NewPost(forms.Form):
    title = forms.CharField(
        label="title", required=True, widget=forms.TextInput(attrs={"placeholder": " eg: New post"}))
    text = forms.CharField(label="post", widget=forms.Textarea(
        attrs={"rows": 3, "cols": 115, "placeholder": " eg: Going out with friends."}), required=True)


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html", {
        "postform": NewPost(),
        "page_obj": page_obj,
    })


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def post(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        try:
            post = Post(title=title, text=text,
                        user=request.user)
            post.save()
        except IntegrityError:
            return render(request, "network/index.html", {
                "postform": NewPost(),
                "error": "Something went wrong, Please try again.",
            })

        return HttpResponseRedirect(reverse("index"))


def user(request, name):

    if request.method == "GET":
        try:
            u = User.objects.get(username=name)
            p = Post.objects.filter(user=u)
            fc = {"following": u.following.count(), "follower": u.follower.count()}

        except IntegrityError as e:
            return render(request, "network/udetails.html", {
                "error": e,
            })
        paginator = Paginator(p, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "network/udetails.html", {
            "u": u,
            "sfollow": True if u.username != request.user.username else False,
            "page_obj": page_obj,
            "fc": fc,
        })


@csrf_exempt
@login_required
def update_user(request, user_id):

    # Query for requested email
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "Email not found."}, status=404)

    # Return email contents
    if request.method == "GET":
        return JsonResponse(user.serialize())

    # Update whether email is read or should be archived
    elif request.method == "PUT":
        data = json.loads(request.body)
        if data.get("read") is not None:
            user.read = data["read"]
        if data.get("archived") is not None:
            user.archived = data["archived"]
        user.save()
        return HttpResponse(status=204)

    # Email must be via GET or PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)


@csrf_exempt
@login_required
def update_post(request, post_id):

    # Query for requested post
    try:
        post = Post.objects.get(pk=post_id)
        like = Like.objects.get(post=post_id, user=request.user)
    except Post.DoesNotExist or Like.DoesNotExist:
        return JsonResponse({"error": "Email not found."}, status=404)

    # Return email contents
    if request.method == "POST":
        pass
    if request.method == "GET":
        return JsonResponse(post.serialize())

    # Update whether post is liked
    elif request.method == "PUT":
        data = json.loads(request.body)
        if data.get("like") is not None:
            like.read = data["read"]

        like.save()
        return HttpResponse(status=204)

    # Email must be via GET, POST or PUT
    else:
        return JsonResponse({
            "error": "GET, PUT or POST request required."
        }, status=400)
