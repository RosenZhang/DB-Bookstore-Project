# -*- coding: utf-8 -*-
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import catalog.views
from django.contrib.auth.forms import User,UsernameField
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

# from django import forms
# class SelfUserCreationForm(forms.ModelForm):
#     error_messages = {
#         'password_mismatch': _("The two password fields didn't match."),
#     }
#     username=forms.CharField(
#         label=_("Username"),
#         strip=False,
#         max_length=30,
#         widget=forms.TextInput(attrs={'size': 20,}))
#     password1=forms.CharField(
#         label=_("Password"),
#         strip=False,
#         max_length=30,
#         widget=forms.PasswordInput(attrs={'size': 20,}))
#     password2=forms.CharField(
#         label=_("Password confirmation"),
#         strip=False,
#         max_length=30,
#         widget=forms.PasswordInput(attrs={'size': 20,}))
#
#     class Meta:
#         model = User
#         fields = ("username",)
#         field_classes = {'username': UsernameField}
#
#     def __init__(self, *args, **kwargs):
#         super(SelfUserCreationForm, self).__init__(*args, **kwargs)
#         if self._meta.model.USERNAME_FIELD in self.fields:
#             self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         self.instance.username = self.cleaned_data.get('username')
#         password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
#         return password2
#
#     def save(self, commit=True):
#         user = super(SelfUserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

def signup(request):
    return render(request,'signup2.html')
# Create your views here.
