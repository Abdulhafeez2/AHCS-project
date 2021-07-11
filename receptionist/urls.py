from django.urls import path
from . import views


urlpatterns = [
    path('',views.receptionist_dashboard,name='receptionist_dashboard'),
    path('registeration/',views.register_new_patinet,name='register_new_patient'),
]
