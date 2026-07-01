from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:user_id>/", views.user_info, name="Student info"),
    path("search/", views.search_student, name="Search student"),
    path("add/", views.add_student, name="Add student"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name = "User login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="index"), name = "User logout")
]