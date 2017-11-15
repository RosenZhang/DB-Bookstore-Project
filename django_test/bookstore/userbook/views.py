from django.shortcuts import render

# Create your views here.
def userbook_view(request):
	template='userbookpage.html'
	context={'books':['book1','book2']}
	return render(request,template,context)