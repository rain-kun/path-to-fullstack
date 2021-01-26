from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    pass


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(default=now)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    

class Division(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    room = models.IntegerField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='divs')
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return str(self.name) + " " + str(self.surname)


