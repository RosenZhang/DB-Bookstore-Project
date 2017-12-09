# Create your views here.

from django.shortcuts import render

from django.shortcuts import render, redirect
from utils.util import get_record_transaction_info
from django.db import connection
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
import datetime
from .forms import addrecord
import catalog.views
import signuppage.views

def storemanager_view(request):
    template='storemanagerindex.html'
    context = {}
    context['record_transaction'] = get_record_transaction_info()
    return render(request,template,context)

def add_transaction_record(request):
    Tid = 'null'
    #print(get_record_transaction_info(Tid))
    available_copy = 0

    if request.method == 'POST':
        form = addrecord(request.POST)
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
            Bid =form.cleaned_data['Bid']
            now = 'now()'
            cursor = connection.cursor()
            #cursor.execute("SET FOREIGN_KEY_CHECKS=1")
            bidlist=list(d['bid'] for d in get_record_transaction_info())
            print(bidlist)
            if Bid in bidlist:
                # if ISBN13 is found in book records
                cursor.execute(("insert into record_transaction(Tid, Tdate, copynum, Bid) values (%s,%s,%s,'%s')" % (
                    Tid, now, copynum, Bid)))
                #cursor.execute(("select * from record_transaction order by Tid ASC"))
                return HttpResponseRedirect(reverse('storemanager'))
            else:
                #when ISBN13 is not found in book record this will be run
                cursor.execute(("insert into books(title,piclink,format,pages,subject,language,authors,publisher,year,isbn10,isbn13,available_copy) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                    %(title,piclink,format,pages,subject,language,authors,publisher,year,isbn10,Bid,available_copy)))
                cursor.execute(("insert into record_transaction(Tid, Tdate, copynum, Bid) values (%s,%s,%s,'%s')" % (
                   Tid, now, copynum, Bid)))
                return HttpResponseRedirect(reverse('storemanager'))
            form.save()

    else:

        form = addrecord()

    return render(request, 'addnewbook.html',{'form':form})


