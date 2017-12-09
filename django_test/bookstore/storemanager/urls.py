from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.storemanager_view, name='storemanager'),
    url(r'^addrecord/$', views.add_record_view, name='add_record'),
    url(r'^addbook/$', views.add_book_view, name='add_book'),
    # a function in views called index will be called. ^s start marker, $ is end marker
    # name is to idenfy the mapping
]