# Generated by Django 2.2.7 on 2019-11-08 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0005_auto_20191107_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='speciality',
            new_name='specialty',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='speciality',
            new_name='specialty',
        ),
    ]
