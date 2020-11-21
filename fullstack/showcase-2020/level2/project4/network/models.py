from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, default='')
    text = models.TextField(max_length=200, null=False, default='')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default='', related_name="postby")
    created_on = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def is_valid_post(self):
        if len(self.title) > 0:
            if len(self.text) > 0:
                return True
        return False

    def get_total_likes(self):
        return self.likes.user.count()


class Like(models.Model):
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, default='', related_name="likes")
    user = models.ManyToManyField(User, default='', related_name="likedby")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.get_total_likes())

#


class Follow(models.Model):
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, default='', related_name="following")
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, default='', related_name="follower")

    class Meta():
        ordering = ["-following"]
