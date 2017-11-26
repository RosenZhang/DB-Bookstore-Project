
from django.shortcuts import render

from .utils import get_book_list


# Create your views here.
def usermainpage_view(request):
	book_list=get_book_list()
	template='userbookpage.html'
	context={'book_list':book_list,'books':['book1','book2']}
	return render(request,template,context)

def book_view(request,ISBN13=None):
	template='book.html'
	context={'book':{'piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','title':'Fred the lonely monster','format':'paperback','ISBN13':ISBN13,"authors":'author_name'},
	'feedbacks':[{'Feedback_giver':'user1','Fcomment':'hi'}],
	'recommendations':[{'title':'a girl','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png'},{'title':'two girls','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png'}]
	}
	return render(request,template,context)

