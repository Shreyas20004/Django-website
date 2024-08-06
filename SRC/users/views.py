from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login



def login_view(request):
    loginForm = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request,data=request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'You are now logged in as {username}')
                return redirect('home')
            else:
                messages.error(request, f'There was an error trying to login')
        else:
            messages.error(request, f'There was an error trying to login')
    elif request.method == 'GET': 
        login_form = AuthenticationForm()
    return render(request, 'views/login.html',{'loginForm':loginForm})
# Create your views here.

def register_view(request):
    return render(request,'views/register.html')