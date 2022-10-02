from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class AddRatingFrom(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.beer = kwargs['instance']
        super().__init__(**kwargs)

    # def save(self, commit=True):
    #     obj = super(AddRatingFrom, self).save(commit=False)
    #     obj.beer = self.beer
    #     if commit:
    #         obj.save()
    #     return obj

    class Meta:
        model = Rating
        fields = ('rate',)


class AddReviewForm(forms.Form):
    pass


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
