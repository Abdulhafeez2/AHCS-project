from django.shortcuts import redirect, render

# Create your views here.

def login(request):
    context={}
    return render(request,'landing-page.html',context)