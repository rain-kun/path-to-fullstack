
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("post", views.post, name="post"),
    path("user/<str:name>", views.user, name="user"),

    # jason update
    path("user/<int:id>", views.update_user, name="update_user"),
    path("post/<int:id>", views.update_post, name="update_post"),
]
