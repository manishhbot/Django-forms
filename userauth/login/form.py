from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Details, Django_user


class Admin(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class Detailss(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'


class Djangouserr(ModelForm):
    class Meta:
        model = Django_user
        fields = ('picture',)
