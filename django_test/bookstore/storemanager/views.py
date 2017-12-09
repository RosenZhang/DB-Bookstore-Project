# Create your views here.

from django.shortcuts import render

from django.shortcuts import render, redirect

from utils.util import get_record_transaction_info, get_order_author_info, get_order_title_info,\
    get_order_publisher_info,check_book_exists,add_new_book_and_transaction,save_transaction
from django.db import connection
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
import datetime
from .forms import addrecord,addbook
import catalog.views
import signuppage.views
import json


from django.contrib.auth.decorators import login_required

@login_required
def storemanager_view(request):
    if request.user.is_superuser:
        template='storemanagerindex.html'
        context = {}
        if request.method == 'POST':
            bid=request.POST['bid']

            book_exists=check_book_exists(bid)

            if book_exists:
                return HttpResponse(json.dumps({'book_exists': True}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'book_exists': False}), content_type="application/json")

        context['record_transaction'] = get_record_transaction_info()
        context['order_author'] = get_order_author_info()
        context['order_title'] = get_order_title_info()
        context['order_publisher'] = get_order_publisher_info()
        return render(request,template,context)
    else:
        return redirect(signuppage.views.signup)

@login_required
def add_record_view(request):
    if request.user.is_superuser:
        template='addnewrecord.html'
        if request.method == 'POST':
            form = addrecord(request.POST)
            if form.is_valid():
                copynum = form.cleaned_data['copynum']
                bid =form.cleaned_data['Bid']
                save_transaction(copynum,bid)
                return HttpResponseRedirect(reverse('storemanager'))
                form.save()

        else:
            form = addrecord()

        return render(request, template,{'form':form})

        return render(request,template,context)

        context['record_transaction'] = get_record_transaction_info()
        return render(request,template,context)
    else:
        return redirect(signuppage.views.signup)

@login_required
def add_book_view(request):
    if request.user.is_superuser:
        available_copy = 0

        if request.method == 'POST':
            form = addbook(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                piclink = form.cleaned_data['piclink']
                format = form.cleaned_data['format']
                pages = form.cleaned_data['pages']
                subject = form.cleaned_data['subject']
                language = form.cleaned_data['language']
                authors = form.cleaned_data['authors']
                publisher = form.cleaned_data['publisher']
                year = form.cleaned_data['year']
                isbn10 = form.cleaned_data['isbn10']
                copynum = form.cleaned_data['copynum']
                bid =form.cleaned_data['Bid']
                now = 'now()'
                add_new_book_and_transaction(title,piclink,format,pages,subject,language,authors,publisher,year,isbn10,bid,available_copy,copynum)

                return HttpResponseRedirect(reverse('storemanager'))
                form.save()

        else:

            form = addbook()

        return render(request, 'addnewbook.html',{'form':form})
    else:
        return redirect(signuppage.views.signup)

