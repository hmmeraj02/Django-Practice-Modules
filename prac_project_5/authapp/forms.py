from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model = User
        fields = ['username', 'name', 'email']