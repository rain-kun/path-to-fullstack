from django.urls import path
from .views import login_view, logout_view, register, index, division, student, CourseAPIView, CourseList, DivisionList\
        , DivisionAPIView, StudentList, StudentAPIView

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
    path('', index, name='index'),
    path('course/<int:id>', division, name='division'),
    path('division/<int:id>', student, name='student'),
    path('api/courses/', CourseList.as_view(), name="csearch"),
    path('api/divisions/', DivisionList.as_view(), name="dsearch"),
    path('api/students/', StudentList.as_view(), name="ssearch"),
    path('api/course/<int:id>', CourseAPIView.as_view(), name="chandle"),
    path('api/division/<int:id>', DivisionAPIView.as_view(), name="dhandle"),
    path('api/student/<int:id>', StudentAPIView.as_view(), name="shandle"),
    # path('api/division/<int:id>', dapi, name="dapi"),
    # path('api/student/<int:id>', sapi, name="sapi"),
]