from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], default=3)

    def __str__(self):
        return self.name
    