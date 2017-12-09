from django.conf.urls import url

from .views import usermainpage_view, book_view,recommendation_view

urlpatterns = [
	url(r'^$', usermainpage_view,name='main'),
	url(r'^(?P<ISBN13>\d*)/recommendations$',recommendation_view),
	url(r'^(?P<ISBN13>\d*)/(?P<topnum>\d*)$',book_view),
]