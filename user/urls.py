from django.urls import path
from .views import *
from django.urls import re_path
urlpatterns = [
    path('',Home.as_view()),
    path('home/',Home.as_view(), name="home"),
    path('login/',UserLogin.as_view(), name="login"),
    path('logout/',UserLogout.as_view(), name="logout"),
    path('sign-up/',UserSignUp.as_view(), name="sign_up"),
    # path('course/enroll/<slug:slug>',EnrollCourse.as_view(), name="enroll_course"),
    re_path(r'^course/enroll/(?P<slug>[-\w]+)$', EnrollCourse.as_view(), name='enroll_course'),
    re_path(r'^course/(?P<slug>[-\w]+)$', DetailedCourseView.as_view(), name='course'),
    # path('course/<slug:slug>',DetailedCourseView.as_view(), name="course"),
    path('my-course/',MyCourse.as_view(), name="my_course"),
]