# Generated by Django 3.0.6 on 2020-07-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200725_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avasco_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Avasco ID (if exists)'),
        ),
    ]
