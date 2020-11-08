from django import forms

class First_form(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField()
    address = forms.CharField(widget= forms.Textarea)
