from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('radiologist_dashboard/',views.radiologist_dashboard,name='radiologist_dashboard'),
]
