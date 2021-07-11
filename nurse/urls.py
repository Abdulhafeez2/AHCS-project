from django.urls import path
from . import views


urlpatterns = [
    path('',views.nurse_dashboard,name='nurse_dashboard'),
    path('add_vital_sign/',views.add_vital_sign,name='add_vital_sign'),
]
