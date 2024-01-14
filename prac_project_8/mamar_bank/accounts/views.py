from django.shortcuts import redirect, render
from django.views.generic import FormView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

def send_transaction_email(user, subject, template):
    # Gather users to notify about the transaction
    message = render_to_string(template, {
            'user': user,
        })
    to_email = user.email
    print(f"Sending email to {to_email} with subject: {subject}")
    print(f"Message: {message}")

    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = "accounts/user_login.html"
    def get_success_url(self):
        return reverse_lazy('home')

def user_logout(request):
    logout(request)
    return redirect('login')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
    
def pass_change(request):
    if request.method == 'POST':
        change_form = PasswordChangeForm(request.user, request.POST)
        if change_form.is_valid():
            change_form.save()
            print(f"pass change")
            messages.success(request, 'Password Changed Successfully!')
            update_session_auth_hash(request, change_form.user)
            send_transaction_email(request.user, "Password Change Message", "accounts/password_email.html")
            return redirect('profile')
    else:
        change_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {'form':change_form})