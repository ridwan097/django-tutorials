from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),   

]