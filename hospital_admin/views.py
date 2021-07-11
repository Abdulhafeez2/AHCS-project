from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from login import urls,decorators
from .utils import *
from django.contrib.auth.models import User,Group


@login_required(login_url='login_url')
@decorators.hospital_adminonly

def hospital_admin_homepage(request):

    context = {}

    return render(request, 'hospital_admin/homepage.html', context)
##############################################################################################################################################
@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['Hospital_admin'])
@decorators.hospital_adminonly
def add_receptionist(request):
    
    if request.method == 'POST':
        form=ReceptionistCreationForm(request.POST)
        
        if form.is_valid():
            new_receptionist=form.save
            context=new_receptionist
            print(context["username"])
            return redirect('hospital_admin_homepage_url')
    else:
         form=ReceptionistCreationForm()       
    context = {'form': form}
    return render(request, 'hospital_admin/receptionists_add.html', context)

################################################################################ 

    # all receptionist
def all_receptionist(request):
    all_receptionist=User.objects.all()
    context={'all_receptionist':all_receptionist}
    return render(request,'forms/all-receptionist.html',context)


######### add nurse  ####################
@decorators.allowed_users(allowed_roles=['Hospital_admin'])
def add_nurse(request):
   if request.method == 'POST':
        form=ReceptionistCreationForm(request.POST)
        
        if form.is_valid():
            new_receptionist=form.save
            context=new_receptionist
            print(context["username"])
            return redirect('hospital_admin_homepage_url')
        else:
            form=ReceptionistCreationForm()       
        context = {'form': form}
        return render(request, 'hospital_admin/receptionists_add.html', context)