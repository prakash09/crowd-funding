from django.shortcuts import render
import datetime
import json
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from .models import Person

# Create your views here.

def landing_page(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    if request.method == 'GET':
        try:
            if request.session['error_msg'] != None:
                msg=request.session['error_msg']
                request.session['error_msg']=None
                return render(request, 'auth_app/index.html',{'error_msg':msg})
            else:
                return render(request, 'auth_app/index.html')
        except:
                return render(request, 'auth_app/index.html')
@csrf_exempt
def sign_up(request):
    data=request.POST
    if request.user.is_authenticated():
    	logout(request)
        request.session['error_msg'] = None
        return redirect('landing_page')
    if request.method == 'GET':
    	logout(request)
        request.session['error_msg'] = None
    	return redirect('landing_page')
    elif request.method == 'POST': 
        import pdb; pdb.set_trace()
        try:
            user = User.objects.create_user(username=data['email'],first_name=data['name'], email = data['email'])
            user.save()
            user.set_password(data['password'])
            user.save()
            profile = Person(user = user,phone=data['phone'])
            profile.save()
            request.session['error_msg'] = None
            return redirect('landing_page')
        except:
            request.session['error_msg'] = "Email already registered"
            return redirect('landing_page')

@csrf_exempt
def sign_in(request):
    data=request.POST
    if request.user.is_authenticated():
        return redirect('dashboard')
    if request.method == 'GET':
        return redirect('landing_page')
    elif request.method == 'POST':
        username =  data['username']
        password = data['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            request.session['error_msg'] = "Userid or password is incorrect"
            return redirect('landing_page')

@login_required(login_url = 'sign_in' )
def sign_out(request):
    logout(request)
    request.session.flush()
    return redirect('landing_page')
