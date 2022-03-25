from cProfile import label
from ssl import HAS_TLSv1_1, HAS_TLSv1_3
from turtle import textinput
from django import forms
from django.contrib.auth.models import User
from django.http import Http404
from .models import Messages
from django.contrib.auth.forms import UserCreationForm

class UserAppealForm(forms.Form):
    
    subject = forms.CharField(label='Тема', required=True)
    from_email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)
    
    # title = forms.CharField(
    #     label= 'Тема', 
    #     max_length=150, 
    #     required=True,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Theme'})
    #     )
    
    # email = forms.EmailField(
    #     label='Введите ваш Email',
    #     required=True,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    # )
    
    # text_message = forms.CharField(
    #     max_length=500,
    #     required=True,
    #     widget=forms.TextInput(attrs={'style': 'height: 170px;'})
    #     )
    
    class Meta:
        model = Messages
        fields = ['title', 'email', 'text_message']
