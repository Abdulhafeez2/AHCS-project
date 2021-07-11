from django.urls import path
from . import views
urlpatterns = [
    path('', views.hospital_admin_homepage,
         name="hospital_admin_homepage_url"),
    path('add_receptionist', views.add_receptionist, name='add_receptionist_url'),
    path('add_nurse',views.add_nurse,name="add_nurse_url"),
    path('all_receptionist',views.all_receptionist,name="all_receptionist_url"),


]
