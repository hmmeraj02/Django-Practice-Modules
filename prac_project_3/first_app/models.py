from django.db import models

# Create your models here.
class Example(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    comment = models.TextField()
    agree = models.BooleanField()
    date = models.DateField()
    birth_date = models.DateField()
    value = models.DecimalField(max_digits=5, decimal_places=2)
    # favorite_color = models.ChoiceField(choices=fav_colors_choices)
    # favorite_color = models.MultipleChoiceField(widget=models.CheckboxSelectMultiple, choices=fav_colors_choices)
    url_field = models.URLField()