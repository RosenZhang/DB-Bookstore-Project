# Create your views here.

from django.shortcuts import render

from utils.util import get_record_transaction_info

def storemanager_view(request,Tid=None):
	template='storemanagerindex.html'
	context = {}
	context['record_transaction'] = get_record_transaction_info('100')
	return render(request,template,context)



