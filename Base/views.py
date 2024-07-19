from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def home(request): 
	return render(request, "home.html") 

def projects(request): 
	return render(request, "projects.html") 

def contact(request): 
	return render(request, "contact.html")

def login_123(request):
	if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
		username = request.POST['username']
		password = request.POST['password']
		print("username is ",username," password is ",password)
		user = authenticate(request, username = username, password = password)
		form_123=None
		if user is not None:
			form_123 = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('home')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form_123 = AuthenticationForm()
	return render(request, 'login.html', {'form':form_123,'title':"Login form"})