from django.contrib import admin

from subscribers.models import Subscriber
from .models import *

class VacancyAdmin(admin.ModelAdmin):
    class Meta:
        model = Vacancy
    list_display = ('title', 'url', 'city', 'specialty', 'timestamp')


class SubscriberAdmin(admin.ModelAdmin):
    class Meta:
        model = Subscriber
    list_display = ('email', 'city', 'specialty', 'is_active')
    list_editable = ['is_active']

# Register your models here.
admin.site.register(City)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Specialty)
admin.site.register(Site)
admin.site.register(Url)
admin.site.register(Subscriber, SubscriberAdmin)

