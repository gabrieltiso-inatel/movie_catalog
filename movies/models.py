from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    release_date = models.DateField()
    duration = models.SmallIntegerField(default=0)

