from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from AccountCreationApp.models import CustomerInfo

# Create your views here.
def Login_Page(request):
    if request.method=="POST":
        username1=request.POST['username']
        password1=request.POST['password']
        x=auth.authenticate(username=username1,password=password1)

        if x is not None:
            auth.login(request,x)
            if CustomerInfo.objects.filter(is_superuser=False):
                return redirect('/account')
            else:
                messages.info(request,'Invalid credentials')
                return redirect('/login')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/login')
    else:
        return render(request,template_name='html/BankLoginApp/Login_Page.html',)



def Admin_Login_Page(request):
    if request.method=="POST":
        username1=request.POST['username']
        password1=request.POST['password']
        x=auth.authenticate(username=username1,password=password1)

        if x is not None:
            auth.login(request,x)
            if CustomerInfo.objects.filter(is_superuser=True):
                return redirect('/Admin_Dashboard')
            else:
                messages.info(request,'Invalid credentials')
                return redirect('/Admin_Login')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/Admin_Login')
    else:
        return render(request,template_name='html/BankLoginApp/Admin_Login_Page.html',)


