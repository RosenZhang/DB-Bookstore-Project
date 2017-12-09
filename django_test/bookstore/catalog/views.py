# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from utils.util import get_order_history, get_user_information,get_feedback_history,get_rating_history

# Create your views here.
from .models import Book, Author, BookInstance, Genre # use to access data

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
import signuppage.views
import storemanager.views

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(catalog_view)
        else:
            pass
            # TODO: prompt a window
    return redirect(signuppage.views.signup)


def login_user(request):
    username = None
    password = None
    if request.method == 'POST':
        for key in request.POST:
            username = request.POST['username_login']
            password = request.POST['password_login']
        user = authenticate(request, username=username, password=password)
        if 'manager_login' in request.POST:
            if user is not None and user.is_superuser:
                return redirect(storemanager.views.storemanager_view)
        else:
            if user is not None:
                login(request, user)
                return redirect(catalog_view)
            else:
                return  redirect(signuppage.views.signup)
    else:
        return redirect(signuppage.views.signup)
        # TODO: prompt a "invalid username and  password combination"


@login_required
def catalog_view(request):
    template = "index.html"
    context = {}
    userid = request.user.id
    context['order_history'] = get_order_history(userid)
    context['user_info'] = get_user_information(userid)
    context['feedback_history'] = get_feedback_history(userid)
    context['rating_history'] = get_rating_history(userid)
    return render(request,template,context)

def logout_user(request):
    logout(request)
    return redirect(signuppage.views.signup)
