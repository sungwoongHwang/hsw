import json

from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import authenticate,login
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from users.models import User



def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        middle_name = request.POST['middlename']
        last_name = request.POST['lastname']
        phone_number = request.POST['phonenumber']
        gender = request.POST['gender']
        date_of_birth = request.POST['birthday']

        user = User.objects.filter(User_name=username)
        if user:
            messages.warning(request,"Sign up failed")

        else:
            User.objects.create(First_name=first_name, Middle_name=middle_name, Last_name=last_name, User_name=username,
                            password=password, phone_number=phone_number, Gender=gender, Date_of_birth=date_of_birth)
            messages.warning(request,"Sign up succeed")
            HttpResponseRedirect("/")
    return render(request, 'users/signUp.html', {})


def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(User_name=username, password=password)
        if user:
            messages.warning(request, "sign-in succeed")

            # HttpResponseRedirect("/")
        else:
            messages.warning(request, "sign-in failed")
    return render(request, 'users/signIn.html',{})

