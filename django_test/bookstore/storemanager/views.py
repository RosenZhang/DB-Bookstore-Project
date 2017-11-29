# Create your views here.

from django.shortcuts import render

def store_manager(request,ISBN13=None):
	template='storemanagerindex.html'
	context={'book':{'piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','title':'Fred the lonely monster','format':'paperback','ISBN13':ISBN13,"authors":'author_name'},
	'feedbacks':[{'Feedback_giver':'user1','Fcomment':'hi','Fdate':'2017-8-17'},{'Feedback_giver':'user2','Fcomment':'byeee','Fdate':'2017-8-17'}],
	'recommendations':[{'title':'a girl','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','ISBN13':'10010101'},{'title':'two girls','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','ISBN13':'10010102'}]
	}
	return render(request,template,context)
