from django.db import models

# Create your models here.

class Tejidomama (models.Model):
   partP = models.IntegerField()
   temperatura= models.FloatField()
   color = models.FloatField()
   inflamacion = models.FloatField()
