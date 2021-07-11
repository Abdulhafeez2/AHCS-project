from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('',views.lab_technician_homepage,name="lab_technician_dashboard_url")
]
