from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm


def home(request): 
	return render(request, "home.html") 

def projects(request): 
	return render(request, "projects.html") 

def contact(request): 
	return render(request, "contact.html")

