from django.urls import path

from . import views

urlpatterns = [
    path("", views.users, name="index"),
    path("<int:user_id>/", views.user_info, name="Student info"),
    path("search/", views.search_student, name="Search student")
]