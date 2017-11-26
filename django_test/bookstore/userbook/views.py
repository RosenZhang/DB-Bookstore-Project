from django.shortcuts import render

from utils.util import my_custom_sql_dict, get_book_info,get_feedback_info


# Create your views here.
def usermainpage_view(request):
	template='userbookpage.html'
	my_custom_sql_dict()
	context={'books':['book1','book2']}
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