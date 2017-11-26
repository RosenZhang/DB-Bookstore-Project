from django.conf.urls import url

from .views import usermainpage_view, book_view

urlpatterns = [
	url(r'^$', usermainpage_view,name='main'),
	url(r'^(?P<ISBN13>\w*)/$',book_view),

]