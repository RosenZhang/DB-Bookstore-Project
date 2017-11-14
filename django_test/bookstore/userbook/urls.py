from django.conf.urls import url

from .views import userbook_view

urlpatterns = [
	url(r'^$', userbook_view),
 
]