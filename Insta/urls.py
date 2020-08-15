# app level's urls.py for URLConfs of app

from django.urls import path

from . import views

urlpatterns = [
    path('', views.HelloDjango.as_view()),
]
