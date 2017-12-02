from django import forms
from django.core.exceptions import ValidationError

class addrecord(forms.Form):
    #Tid = forms.CharField(required=True)
    #Tdate =forms.DateField(required=True)
    copynum =forms.CharField(required=True)
    Bid =forms.CharField(required=True)




