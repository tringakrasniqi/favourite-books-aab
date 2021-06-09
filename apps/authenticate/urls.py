from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # GET request
    path('login', views.login),  # POST request
    path('register', views.register),  # POST request
    path('logout', views.logout)  # POST request
]
