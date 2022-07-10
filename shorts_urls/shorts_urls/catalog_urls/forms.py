from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Catalog_Urls


class RegUsers(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)


class InOutLink(forms.ModelForm):
    class Meta:
        model = Catalog_Urls
        fields = ['long_link']
