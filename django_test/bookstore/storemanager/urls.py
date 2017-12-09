from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.storemanager_view, name='storemanager'),
    url(r'^added/$', views.add_transaction_record, name='add_transaction_record'),
#url(r'^validate_Tid/$', views.validate_Tid, name='validate_Tid'),
    # a function in views called index will be called. ^s start marker, $ is end marker
    # name is to idenfy the mapping
]