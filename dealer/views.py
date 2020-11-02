from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.



def login(request):
    if request.user.is_authenticated:
        return redirect('dealer_dashboard')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff == 1:
                auth.login(request,user)
                if user.is_staff == 1:
                    return redirect('dealer_dashboard')
            else:
                messages.error(request, 'Invalid username and password')
                return redirect('login')

        else:
            messages.error(request, 'Invalid username and password')
            return redirect('login')
    else:
       return render(request,'login.html')

        

@login_required(login_url='/')
def dealer_dashboard(request):

        return render(request,'dealer_dashboard.html')    


def logout(request):
    auth.logout(request)
    return redirect('login')