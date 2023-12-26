from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.
def home(request):
    if request.method == 'POST':
        example = forms.ContactForm(request.POST)
        if example.is_valid():
            example.save()
    else:
        example = forms.ExampleForm()
    return render(request, 'home.html', {'data' : example})