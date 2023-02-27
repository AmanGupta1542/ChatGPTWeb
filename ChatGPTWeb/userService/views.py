from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def login_request(request):
    # if request.user.is_active: return redirect('/')
    if 'loggedinUser' in request.session: return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        currentUser = authenticate(username=username, password=password)
        if currentUser is not None:
            login(request, currentUser)
            request.session['loggedinUser'] = username
            # uObj = User.objects.get(username=request.user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credential!!!' ,extra_tags='notmatch')
    return render(request, 'userService/login.html')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/user/login")