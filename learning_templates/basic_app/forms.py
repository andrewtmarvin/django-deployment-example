from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


class UserForm(forms.ModelForm):
        username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Username"}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

        class Meta():
            model = User
            fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')