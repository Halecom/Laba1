from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("register/", views.register),
    path("logout/", views.logout),
    # path("edit/<int:id>/", views.edit),
    # path("delete/<int:id>/", views.delete),
    path("authorization/", views.authorization),
    path("password_change/", views.password_change),
]
