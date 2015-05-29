# _*_ coding: utf-8 _*_
from django import forms
from models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']