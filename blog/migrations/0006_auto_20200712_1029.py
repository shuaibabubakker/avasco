# Generated by Django 3.0.6 on 2020-07-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200712_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='occupation_or_course',
            field=models.CharField(default='Student', max_length=100, null=True),
        ),
    ]