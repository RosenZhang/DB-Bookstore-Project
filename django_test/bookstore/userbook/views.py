
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from utils.util import get_book_list, get_book_list_v2_with_brief_record, get_book_info,\
    get_feedback_info,save_user_usefulness_rating, save_user_order, return_user_usefulness_rate,\
    check_user_has_posted_feedback, save_user_feedback, get_feedback_info_with_limit

# Create your views here.
@login_required
def usermainpage_view(request):
    # book_list=get_book_list()
    template='userbookpage.html'
    book_list, books = get_book_list_v2_with_brief_record('a')
    # books = [{'title':'book1','ISBN13':'1028374','authors':"author1", 'publisher':"publisher1"},
		# {'title':'book2','ISBN13':'1028375','authors':"author2", 'publisher':"publisher1"}]
    context={'book_list':book_list,'books':books}
    return render(request,template,context)

@login_required
def book_view(request,ISBN13=None,topnum=None):
	userid=request.user.id
	template='book.html'
	context = {}
    # check if user has rated the book
	context['userhasrated']=check_user_has_posted_feedback(userid,ISBN13)
	context['book'] =get_book_info(ISBN13)
	if topnum=='':
		context['feedbacks'] = get_feedback_info(ISBN13, userid)
	else:
		context['feedbacks'] = get_feedback_info_with_limit(ISBN13, userid,topnum)
	# print("feedback information ===========================--------------", context['feedbacks'])
	if 'HTTP_FEEDBACK_RATING' in request.META:
		Fid=request.POST['Fid']
		score=request.POST['score']
		save_user_usefulness_rating(Fid,score,userid)
	elif 'HTTP_BOOK_RATING' in request.META:
		rank=request.POST['rank']
		Fcomment=request.POST['Fcomment']
		save_user_feedback(userid,ISBN13,rank,Fcomment)
	elif 'HTTP_ORDER_BOOK' in request.META:
		copynum=request.POST['copynum']
		print(userid,copynum,ISBN13)
		save_user_order(userid,copynum,ISBN13)
		

    # context={'book':{'piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','title':'Fred the lonely monster','format':'paperback','ISBN13':ISBN13,"authors":'author_name'},
    # 'feedbacks':[{'Feedback_giver':'user1','Fcomment':'hi'}],
    # 'recommendations':[{'title':'a girl','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png'},{'title':'two girls','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png'}]
    # }
	return render(request, template, context)

