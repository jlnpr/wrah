# Generated by Django 4.2.16 on 2024-12-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0004_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='plec',
            field=models.IntegerField(choices=[(1, 'Kobieta'), (2, 'Męzczyzna'), (3, 'Inna')], default=3),
        ),
    ]
