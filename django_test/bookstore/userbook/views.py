
from django.shortcuts import render


from utils.util import get_book_list, get_book_info,get_feedback_info



# Create your views here.
def usermainpage_view(request):
	book_list=get_book_list()
	template='userbookpage.html'
	books=[{'title':'book1','ISBN13':'1028374','authors':"author1"},{'title':'book2','ISBN13':'1028375','authors':"author2"}]
	context={'book_list':book_list,'books':books}
	return render(request,template,context)

def book_view(request,ISBN13=None):
	template='book.html'
	context = {}
	context['book'] =get_book_info("978-0684801520")
	context['feedbacks'] = get_feedback_info()
	# context={'book':{'piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','title':'Fred the lonely monster','format':'paperback','ISBN13':ISBN13,"authors":'author_name'},
	# 'feedbacks':[{'Feedback_giver':'user1','Fcomment':'hi'}],
	# 'recommendations':[{'title':'a girl','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png'},{'title':'two girls','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png'}]
	# }
	return render(request, template, context)

