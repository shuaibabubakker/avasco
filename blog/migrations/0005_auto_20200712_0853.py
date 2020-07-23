# Generated by Django 3.0.6 on 2020-07-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200712_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='blood_group',
            field=models.CharField(choices=[(1, 'A+'), (2, 'A-'), (3, 'B+'), (4, 'B-'), (5, 'AB+'), (6, 'AB-'), (7, '0+'), (8, 'O-'), (9, 'OTHERS')], default=1, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='city',
            field=models.CharField(default='Thrissur', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='country',
            field=models.CharField(default='India', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='current_location',
            field=models.URLField(default='https://maps.app.goo.gl/aSoSHUyyFsuMZMsB6', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='occupation_or_course',
            field=models.CharField(default='Student', max_length=100, null=True, verbose_name='Occupation/Course'),
        ),
        migrations.AlterField(
            model_name='member',
            name='place',
            field=models.CharField(default='Aviyoor, Edakkara P.O', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='section',
            field=models.CharField(choices=[(1, 'INDIA'), (2, 'GCC')], default=1, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')], default=1, max_length=10, null=True),
        ),
    ]