from django import forms


class FormModel(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

    
