from django.shortcuts import render

# Create your views here.
def usermainpage_view(request):
	template='userbookpage.html'
	context={'books':['book1','book2']}
	return render(request,template,context)

def book_view(request,ISBN13=None):
	template='book.html'
	context={'book':{'piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','title':'mytitle','format':'paperback','ISBN13':ISBN13,"authors":'author_name'},'feedbacks':[{'Feedback_giver':'user1','Fcomment':'hi'}]}
	return render(request,template,context)

