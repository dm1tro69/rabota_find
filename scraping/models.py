from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']


class Specialty(models.Model):
    name = models.CharField(max_length=100, verbose_name='Специальность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Site(models.Model):
    name = models.CharField(max_length=100, verbose_name='Сайт для поиска')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сайт для поиска'
        verbose_name_plural = 'Сайты для поиска'



class Url(models.Model):
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, verbose_name='Специальность', on_delete=models.CASCADE)
    site = models.ForeignKey(Site, verbose_name='Сайт для поиска', on_delete=models.CASCADE)
    url_address = models.CharField(max_length=250, unique=True, verbose_name='Адрес для поиска')
    def __str__(self):
        return 'Специальность {} в г. {} на сайте {}'.format(self.specialty, self.city, self.site)

    class Meta:
        verbose_name = 'Адрес для поиска'
        verbose_name_plural = 'Адреса для поиска'
#
#
#
#
class Vacancy(models.Model):
    url = models.CharField(max_length=250, unique=True, verbose_name='Интернет адрес вакансии')
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
    description = models.TextField(verbose_name='Описание вакансии', blank=True)
    company = models.CharField(max_length=250, verbose_name='Название компании', blank=True)
    city = models.ForeignKey(City, verbose_name='Город', blank=True, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, verbose_name='Специальность', on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

