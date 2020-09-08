from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.


def home_page(request):
    return render(request,'base.html')

def login_page(request):
    return render(request,'registration/login.html')

def bank_page(request):
    return render(request,'home.html')
