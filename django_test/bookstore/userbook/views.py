
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from utils.util import get_book_list, get_book_info,\
	get_feedback_info,save_user_usefulness_rating, save_user_order, return_user_usefulness_rate,get_book_recommendation




# Create your views here.
@login_required
def usermainpage_view(request):
	book_list=get_book_list()
	template='userbookpage.html'
	books=[{'title':'book1','ISBN13':'1028374','authors':"author1"},{'title':'book2','ISBN13':'1028375','authors':"author2"}]
	context={'book_list':book_list,'books':books}
	return render(request,template,context)

@login_required
def book_view(request,ISBN13=None):
	userid=request.user.id
	if 'HTTP_X_UPDATE' in request.META:
		Fid=request.POST['Fid']
		score=request.POST['score']
		save_user_usefulness_rating(Fid,score,userid)
	elif request.method=='POST':
		copynum=request.POST['copynum']
		print(userid,copynum,ISBN13)
		save_user_order(userid,copynum,ISBN13)
	template='book.html'
	context = {}
	context['book'] =get_book_info("978-1449389673")
	context['feedbacks'] = get_feedback_info("978-1449389673", userid)
	print("feedback information ===========================--------------", context['feedbacks'])

	# context={'book':{'piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','title':'Fred the lonely monster','format':'paperback','ISBN13':ISBN13,"authors":'author_name'},
	# 'feedbacks':[{'Feedback_giver':'user1','Fcomment':'hi'}],
	# 'recommendations':[{'title':'a girl','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png'},{'title':'two girls','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png'}]
	# }
	return render(request, template, context)

@login_required
def recommendation_view(request,ISBN13=None):
    template = 'recommendation_template.html'
    context = {}
    context["recommendations"] = get_book_recommendation()
    return render(request, template, context)

