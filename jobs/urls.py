from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:role_id>/", views.role, name="role"),
]
