from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("new/", views.new, name="new"),
    path("logout/", views.logout, name="logout"),
    path("remove/<int:id>", views.remove, name="remove"),
    path("classes/", views.classes, name="classes"),
    path("classes/remove/<int:id>", views.remove_class, name="remove_class")
]