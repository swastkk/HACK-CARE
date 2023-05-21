from django.db import models

# Create your models here.

class HospitalQuery(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    radius = models.IntegerField()

class Disease(models.Model):
    name= models.CharField(max_length=100)
    symptoms = models.TextField()

    def __str__(self):
        return self.name