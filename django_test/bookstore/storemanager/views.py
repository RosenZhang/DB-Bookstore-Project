# Create your views here.

from django.shortcuts import render

from utils.util import get_record_transaction_info, get_book_info
from django.db import connection
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from .forms import addrecord

def storemanager_view(request,Tid=None):
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
            #and (d['Bid'] == 'Bid' for d in get_record_transaction_info(Tid)):
			#Tid = form.cleaned_data['Tid']
			#Tdate = form.cleaned_data['Tdate']
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


            #if Bid in get_record_transaction_info.bid.values():
            # if not any(d['Bid'] == 'Bid' for d in get_record_transaction_info.record_transaction_result):
            #     form = addrecord()
            #
            # else:
            cursor = connection.cursor()
            #cursor.execute("SET FOREIGN_KEY_CHECKS=1")
            for d in get_record_transaction_info():
                print(d['bid'])
                if d['bid']==Bid:
                    print('hi')

                    #if ISBN13 is found in book records
                    cursor.execute(("insert into record_transaction(Tid, Tdate, copynum, Bid) values (%s,%s,%s,'%s')" % (
                    Tid, now, copynum, Bid)))
                    return HttpResponseRedirect(reverse('storemanager'))
                else:
                    print ("hello")
                    #when ISBN13 is not found in book record this will be run
                    cursor.execute(("insert into books(title,piclink,format,pages,subject,language,authors,publisher,year,isbn10,isbn13,available_copy) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                    %(title,piclink,format,pages,subject,language,authors,publisher,year,isbn10,Bid,available_copy)))
                    cursor.execute(("insert into record_transaction(Tid, Tdate, copynum, Bid) values (%s,%s,%s,'%s')" % (
                   Tid, now, copynum, Bid)))
                    return HttpResponseRedirect(reverse('storemanager'))
                    #form = addrecord()

            form.save()
            
    else:

        form = addrecord()

    return render(request, 'addnewbook.html',{'form':form})

#
# def validate_Tid(request):
# 	Tid = request.GET.get('Tid', None)
# 	data = {
# 		'is_taken': get_record_transaction_info.objects.filter(Tid__iexact=Tid).exists()
# 	}
# 	if data['is_taken']:
# 		data['error_message'] = 'A user with this username already exists.'
#
# 	return JsonResponse(data)

