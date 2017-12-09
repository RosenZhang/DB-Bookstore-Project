from django import forms
from django.core.exceptions import ValidationError

class addrecord(forms.Form):

    title =forms.CharField()
    piclink = forms.CharField()
    format = forms.CharField()
    pages = forms.CharField()
    subject = forms.CharField()
    language = forms.CharField()
    authors = forms.CharField()
    publisher = forms.CharField()
    year = forms.CharField()
    isbn10 = forms.CharField()
    copynum =forms.CharField(required=True)
    Bid =forms.CharField(required=True)





