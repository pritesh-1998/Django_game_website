# Generated by Django 2.1 on 2021-09-23 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
