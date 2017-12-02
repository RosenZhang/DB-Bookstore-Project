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
	context['record_transaction'] = get_record_transaction_info(Tid)
	return render(request,template,context)


def add_transaction_record(request):
    Tid = 'null'

    if request.method == 'POST':
        form = addrecord(request.POST)
        if form.is_valid():
			#Tid = form.cleaned_data['Tid']
			#Tdate = form.cleaned_data['Tdate']
            copynum = form.cleaned_data['copynum']
            Bid =form.cleaned_data['Bid']
            now = 'now()'
            cursor = connection.cursor()
            cursor.execute(("insert into record_transaction(Tid, Tdate, copynum, Bid) values (%s,%s,%s,'%s')"%(Tid,now, copynum, Bid)))

            return HttpResponseRedirect(reverse('storemanager'))
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

