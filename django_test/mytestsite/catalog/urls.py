from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # a function in views called index will be called. ^s start marker, $ is end marker
    # name is to idenfy the mapping
]