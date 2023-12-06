from django.urls import path
from . import views

urlpatterns = [
    path("storeHome/", views.storeHome, name="storeHome"),
]