# Create your views here.

from django.shortcuts import render

def store_manager(request,ISBN13=None):
	template='storemanagerindex.html'
	context={'book':{'piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','title':'Fred the lonely monster','format':'paperback','ISBN13':ISBN13,"authors":'author_name'},
	'feedbacks':[{'Feedback_giver':'user1','Fcomment':'hi','Fdate':'2017-8-17'},{'Feedback_giver':'user2','Fcomment':'byeee','Fdate':'2017-8-17'}],
	'recommendations':[{'title':'a girl','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','ISBN13':'10010101'},{'title':'two girls','piclink':'https://about.canva.com/wp-content/uploads/sites/3/2015/01/children_bookcover.png','ISBN13':'10010102'}]
	}
	return render(request,template,context)

# import sys
# sys.path.insert(0,'/Users/elainecheong/Desktop/Development/yourenv/Project/django_test/bookstore/catalog')
# #import Book, BookInstance, Author
# import models.py
#


# def index(request):
#     """
#     View function for home page of site.
#     """
#     # Generate counts of some of the main objects
#     num_books = Book.objects.all().count()
#     num_instances = BookInstance.objects.all().count()
#     # Available books (status = 'a')
#     num_instances_available = BookInstance.objects.filter(status__exact='a').count()
#     num_authors = Author.objects.count()  # The 'all()' is implied by default.
#
#     # Render the HTML template index.html with the data in the context variable
#     return render(
#         request,
#         'index.html',
#         context={'num_books': num_books, 'num_instances': num_instances,
#                  'num_instances_available': num_instances_available, 'num_authors': num_authors},
#     )
