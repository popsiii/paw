# Generated by Django 5.1.2 on 2024-10-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paw_app', '0007_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='plec',
            field=models.IntegerField(choices=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inne')]),
        ),
    ]