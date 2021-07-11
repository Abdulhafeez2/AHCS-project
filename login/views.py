from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
# Create your views here.

from django.contrib import messages


def loginpage(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('hospital_admin_homepage_url')
        else:
            messages.info(request,"Username OR Password incorrect")
            
       
    context={}
    return render(request,'landing-page.html',context)




def logoutuser(request):
    logout(request)
    return redirect('login_url')
    