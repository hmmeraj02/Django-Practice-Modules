from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form':register_form, 'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged In Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, "Username or Password is incorrect")
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form':form, 'type':'Login'})

@login_required
def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')

def pass_change1(request):
    if request.method == 'POST':
        change_form = PasswordChangeForm(request.user, request.POST)
        if change_form.is_valid():
            change_form.save()
            messages.success(request, 'Password Changed Successfully!')
            update_session_auth_hash(request, change_form.user)
            return redirect('profile')
    else:
        change_form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form':change_form})

def pass_change2(request):
    if request.method == 'POST':
        change_form = SetPasswordForm(request.user, request.POST)
        if change_form.is_valid():
            change_form.save()
            messages.success(request, 'Password Changed Successfully!')
            update_session_auth_hash(request, change_form.user)
            return redirect('profile')
    else:
        change_form = SetPasswordForm(request.user)
    return render(request, 'pass_change.html', {'form':change_form})