from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginpage,name="login_url" ),
    path('logout/',views.logoutuser,name="logout_url")
]
