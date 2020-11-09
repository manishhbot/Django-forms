# from django import forms
from django.forms import ModelForm
from pip._vendor.urllib3 import fields

from .models import Details


class Newfile(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
