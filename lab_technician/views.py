from django.shortcuts import render
from login import urls
from django.contrib.auth.decorators import login_required
from login import decorators
# Create your views here.
@login_required(login_url='login_url')
@decorators.lab_technicianonly
def lab_technician_homepage(request):
    
    context={}
    return render(request,'lab_technician_dashboard.html',context)