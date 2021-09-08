from django.db import models

# Create your models here.
class Tracker(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    servings = models.CharField(max_length=25)
    calories = models.CharField(max_length=25)