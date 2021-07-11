from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login import decorators
# Create your views here.



@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['Receptionist'])
@decorators.receptionistonly
def receptionist_dashboard(request):
    context={}
    return render(request,"receptionist/receptionist_dashboard.html",context)

def register_new_patinet(request):
    context={}
    return render(request,"receptionist/form/registeration_form.html",context)