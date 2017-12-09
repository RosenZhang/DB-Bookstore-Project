# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from .models import Book, Author, BookInstance, Genre # use to access data

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
import signuppage.views

@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML templates index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(index)
        else:
            pass
            # TODO: prompt a window
    return redirect(signuppage.views.signup)

def login_user(request):
    if request.method == 'POST':
        for key in request.POST:
            username = request.POST['username_login']
            password = request.POST['password_login']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            return  redirect(signuppage.views.signup)
    else:
        return redirect(signuppage.views.signup)
        # TODO: prompt a "invalid username and  password combination"

def logout_user(request):
    logout(request)
    return redirect(signuppage.views.signup)