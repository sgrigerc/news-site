from cProfile import label
from ssl import HAS_TLSv1_1, HAS_TLSv1_3
from turtle import textinput
from django import forms
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from .models import Messages

class UserAppealForm(forms.Form):
    mes_subject = forms.CharField(
        label= 'Тема письма', 
        max_length=150, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-input'})
        )
    
    email = forms.EmailField(
        label='Введите ваш Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    
    text_message = forms.CharField(
        label= 'Текст сообщения',
        max_length=500,
        required=True,
        widget=forms.TextInput(attrs={'class': 'bs-docs-example form-inline', 'placeholder': 'Text message'})
        )
    
    # class Meta:
    #     model = Messages
    #     fields = ['mes_subject', 'email', 'text_message']
