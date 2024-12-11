# Generated by Django 4.2.16 on 2024-12-11 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0002_person_pseudonim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=80)),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=40)),
                ('nazwisko', models.CharField(max_length=60)),
                ('plec', models.CharField(choices=[('K', 'Kobieta'), ('M', 'Męzczyzna'), ('I', 'Inna')], default='I', max_length=1)),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folder_aplikacji.stanowisko')),
            ],
        ),
    ]