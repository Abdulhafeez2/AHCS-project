from django.shortcuts import render
from login import urls
from django.contrib.auth.decorators import login_required
from login import decorators

# Create your views here.
@login_required(login_url='login_url')
@decorators.radiologistonly
def radiologist_dashboard(request):
    context={ }
    return render(request,"radiologist/radiologist_dashboard.html",context)
