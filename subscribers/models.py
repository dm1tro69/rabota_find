from django.db import models
from scraping.models import *

# Create your models here.


class Subscriber(models.Model):
    email = models.CharField(max_length=100, unique=True, verbose_name='Емайл')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name='Специальность')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    is_active = models.BooleanField(default=True, verbose_name='Получать рассылку?')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Подписчики'
        verbose_name = 'Подписчик'
