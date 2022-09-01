from django.db import models
# Create your models here.
class offer (models.Model):
    name = models.CharField(max_length=25)
    stock = models.IntegerField()
    price = models.FloatField()
    Image = models.CharField(max_length=2500)

