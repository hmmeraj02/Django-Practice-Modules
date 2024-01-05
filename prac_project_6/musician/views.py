from . import forms
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class MusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')    
class MusicianEditView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = "musician.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

@method_decorator(login_required, name='dispatch')
class MusicianDeleteView(DeleteView):
    model = models.Musician
    template_name = "delete_confirmation.html"
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'