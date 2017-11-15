from django.shortcuts import render

# Create your views here.
def usermainpage_view(request):
	template='userbookpage.html'
	context={'books':['book1','book2']}
	return render(request,template,context)
def book_view(request,book_view):
	template='userbookpage.html'
	context={'books':['book1','book2']}
	return render(request,template,context)

