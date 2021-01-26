from django.urls import path, re_path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^wiki/(?P<pagename>\w+)/$', views.pages, name="pages"),
    path("newpage/", views.newpage, name="newpage"),
    path("random/", views.rand_entry, name="random"),
    re_path(r'^edit_entry/(?P<name>\w+)/$', views.edit_entry, name="edit_entry")
    # path("wiki/<str:name>", views.pages, name="pages")
]
