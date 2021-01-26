from django.contrib import admin
from .models import User, Course, Division, Student
# Register your models here.

admin.site.register(User)

admin.site.register(Course)

admin.site.register(Division)

admin.site.register(Student)
