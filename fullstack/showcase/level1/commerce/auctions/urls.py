from django.urls import path, re_path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_list", views.newlist, name="newlist"),
    re_path(r'^categories/(?P<name>\w+)/$', views.categories, name="categories"),
    path("view/<int:id>/", views.viewdetail, name="details"),
    path("status/<int:id>/", views.savestatus, name="savestatus"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist-hangle/<int:id>", views.watchlist_handle, name="watchlist_handle"),
    # path("watchlist_add/<int:id>", views.watchlist_add, name="watchlist_add"),
    # path("watchlist_remove/<int:id>", views.watchlist_remove, name="watchlist_remove"),
    path("comment/<int:id>", views.comments, name="comments"),
    path("view-from-watchlist/<str:title>", views.viewfromwatchlist, name="viewfromwatchlist"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
