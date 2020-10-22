from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

from .models import Register

# Create your views here.

def login(request):
    return render(request, "login.html", {'parameter':'Login'})

def dashboard(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, "dashboard.html")
        else:
            messages.info(request,"Invalid User")
            #return render(request, "dashboard.html", locals())
            return render(request, "login.html")


def signup(request):

    return render(request, "register.html")

def register(request):

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        passwordConfirmed = request.POST['passwordConfirmed']

        if password != passwordConfirmed:
            messages.info(request, 'Password not matching')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return render(request, "dashboard.html")
    else:
        return render(request, "register.html")


    