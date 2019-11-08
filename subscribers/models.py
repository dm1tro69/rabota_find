from django.db import models
from scraping.models import *

# Create your models here.


class Subscriber(models.Model):
    email = models.CharField(max_length=100, unique=True, verbose_name='Емайл')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name='Специальность')
