from django.shortcuts import render
from catalog.util import try_to_save_a_genre, my_custom_sql

# Create your views here.
def userbook_view(request):
	try_to_save_a_genre()
	row = my_custom_sql()
	template='userbookpage.html'
	context={'books':['book1',row]}
	return render(request,template,context)