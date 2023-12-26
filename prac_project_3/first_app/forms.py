from django import forms
from .models import Example
import datetime

fav_colors_choices = [
    ("red", "Red"),
    ("blue", "Blue"),
    ("green", "Green"),
]

class ExampleForm(forms.ModelForm):
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=fav_colors_choices)
    multiple_favorite_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=fav_colors_choices)
    class Meta:
        model = Example
        fields = '__all__'
        labels = {
            # "name": "Your Name",
        }
        help_texts = {
            "email": "Please enter your email address.",
        }
        widgets = {
            "comment": forms.Textarea(attrs={'rows':3}),
            "birth_date": forms.NumberInput(attrs={'type':'date'}),
            # "favorite_color": forms.RadioSelect,
        }