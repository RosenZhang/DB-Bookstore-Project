from django.http import HttpResponse
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

from utils.util import get_book_list, get_book_list_v2_with_brief_record, get_book_info, \
    get_feedback_info, save_user_usefulness_rating, save_user_order, return_user_usefulness_rate, \
    check_user_has_posted_feedback, save_user_feedback, get_feedback_info_with_limit,get_book_recommendation



@login_required
def usermainpage_view(request):
    # book_list=get_book_list()
    template = 'userbookpage.html'

    if 'HTTP_SEARCH_BOOK' in request.META:
        search_title = request.POST['search_title']
        op1=request.POST['op1']
        search_author = request.POST['search_author']
        op2=request.POST['op2']
        search_publisher = request.POST['search_publisher']
        op3=request.POST['op3']
        search_subject = request.POST['search_subject']
        sorted_by=request.POST['sorted_by']
        book_list, books = get_book_list_v2_with_brief_record(search_title,op1,search_author,op2,search_publisher,op3,search_subject,sorted_by)
        return HttpResponse(json.dumps({'books': books}), content_type="application/json")

    else:
        pass
    book_list = get_book_list()
    context = {'book_list': book_list}
    return render(request, template, context)


@login_required
def book_view(request, ISBN13=None, topnum=None):
    userid = request.user.id
    template = 'book.html'
    context = {}
    # check if user has rated the book
    context['userhasrated'] = check_user_has_posted_feedback(userid, ISBN13)
    context['book'] = get_book_info(ISBN13)
    if topnum == '':
        context['feedbacks'] = get_feedback_info(ISBN13, userid)
    else:
        context['feedbacks'] = get_feedback_info_with_limit(ISBN13, userid, topnum)

    if 'HTTP_FEEDBACK_RATING' in request.META:
        Fid = request.POST['Fid']
        score = request.POST['score']
        save_user_usefulness_rating(Fid, score, userid)
    elif 'HTTP_BOOK_RATING' in request.META:
        rank = request.POST['rank']
        Fcomment = request.POST['Fcomment']
        save_user_feedback(userid, ISBN13, rank, Fcomment)
    elif 'HTTP_ORDER_BOOK' in request.META:
        copynum = request.POST['copynum']
        save_user_order(userid, copynum, ISBN13)
    return render(request, template, context)

@login_required
def recommendation_view(request,ISBN13=None,topnum=None):
    template = 'recommendation_template.html'
    context = {}
    context["recommendations"] = get_book_recommendation(ISBN13)
    return render(request, template, context)

