from . import forms
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)