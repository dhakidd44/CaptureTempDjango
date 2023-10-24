from django.db import models

# Create your models here.
class DonneeCapteur(models.Model):
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)