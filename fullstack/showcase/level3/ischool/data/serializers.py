from rest_framework import serializers
from .models import Course, Division, Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ()


class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = '__all__'
        read_only_fields = ()


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ()