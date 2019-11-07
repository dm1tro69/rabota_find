

# Create your views here.
from django.db import IntegrityError
from django.shortcuts import render
from scraping.utils import *
from scraping.models import *
import datetime

def index(request):
    return render(request, 'base.html')

def lists(request):
    today = datetime.date.today()
    city = City.objects.get(name='Львов')
    speciality = Specialty.objects.get(name='Python')
    qs = Vacancy.objects.filter(city=city.id, speciality=speciality.id, timestamp=today)
    if qs:
        return render(request, 'scraping/list.html', {'jobs': qs})
    return render(request, 'scraping/list.html')


def home(request):
    city = City.objects.get(name='Киев')
    speciality = Specialty.objects.get(name='Python')
    url_qs = Url.objects.filter(city=city, speciality=speciality)
    site = Site.objects.all()
    url_w = url_qs.get(site=site.get(name='Work.ua')).url_address
    url_dj = url_qs.get(site=site.get(name='Djinni.co')).url_address
    url_r = url_qs.get(site=site.get(name='Rabota.ua')).url_address
    url_dou = url_qs.get(site=site.get(name='Dou.ua')).url_address
    jobs = []
    jobs.extend(djinni(url_dj))
    jobs.extend(rabota(url_r))
    jobs.extend(work(url_w))
    jobs.extend(dou(url_dou))

    # v = Vacancy.objects.filter(city=city.id, speciality=speciality.id).values('url')
    # url_list = [i['url'] for i in v]
    for job in jobs:
        #if job['href'] not in url_list:
        vacancy = Vacancy(city=city, speciality=speciality, url=job['href'],title=job['title'], description=job['descript'], company=job['company'])
        try:
           vacancy.save()
        except IntegrityError:
            pass


    return render(request, 'scraping/list.html', {'jobs': jobs})

