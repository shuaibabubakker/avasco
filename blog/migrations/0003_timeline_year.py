# Generated by Django 3.0.6 on 2020-07-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200711_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
