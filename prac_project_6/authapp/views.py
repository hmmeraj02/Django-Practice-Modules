from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form':register_form, 'type':'Register'})

class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    
def user_logout(request):
    logout(request)
    return redirect("login")