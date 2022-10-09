from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.images import get_image_dimensions
# from django.forms.widgets import NumberInput

from .models import *


class AddRatingFrom(forms.ModelForm):
    rate = forms.FloatField(label='Рейтинг', widget=forms.NumberInput(attrs={'style': 'width:5ch'}))

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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

    # def clean_avatar(self):
    #     avatar = self.cleaned_data['avatar']
    #     try:
    #         w, h = get_image_dimensions(avatar)
    #
    #         max_width = max_height = 100
    #         if w > max_width or h > max_height:
    #             raise forms.ValidationError(f'Please use an image that is {max_width} pixels'
    #                                         f'or smaller')
    #
    #         main, sub = avatar.content_type.split('/')
    #         if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
    #             raise forms.ValidationError(f'Please use a JPEG, GIF or PNG image')
    #
    #         if len(avatar) > (28 * 1024):
    #             raise forms.ValidationError(f'Avatar file size may not exced 20k')
    #
    #     except AttributeError:
    #         pass
