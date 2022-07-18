from django.db import models

# Create your models here.
class Prices(models.Model):
    open_price = models.CharField(max_length=255)
    higher_price = models.CharField(max_length=255)
    lower_price = models.CharField(max_length=255)
    variation = models.CharField(max_length=255)