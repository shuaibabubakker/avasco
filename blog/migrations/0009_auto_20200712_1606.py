# Generated by Django 3.0.6 on 2020-07-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200712_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='blood_group',
            field=models.IntegerField(choices=[(1, 'A+'), (2, 'A-'), (3, 'B+'), (4, 'B-'), (5, 'AB+'), (6, 'AB-'), (7, '0+'), (8, 'O-'), (9, 'OTHERS')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='city',
            field=models.CharField(blank=True, default='Thrissur', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='company_or_institution_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Company/Institution Name'),
        ),
        migrations.AlterField(
            model_name='member',
            name='company_or_institution_place',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Company/Institution Place'),
        ),
        migrations.AlterField(
            model_name='member',
            name='country',
            field=models.CharField(blank=True, default='India', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='current_location',
            field=models.URLField(blank=True, default='https://maps.app.goo.gl/aSoSHUyyFsuMZMsB6', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='occupation_or_course',
            field=models.CharField(blank=True, default='Student', max_length=100, null=True, verbose_name='Occupation/Course'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_1_india',
            field=models.IntegerField(blank=True, null=True, verbose_name='Indian Phone (if exists)'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_2_gcc',
            field=models.IntegerField(blank=True, null=True, verbose_name='GCC Phone (if exists)'),
        ),
        migrations.AlterField(
            model_name='member',
            name='place',
            field=models.CharField(blank=True, default='Aviyoor, Edakkara P.O', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='section',
            field=models.IntegerField(choices=[(1, 'INDIA'), (2, 'GCC')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')], default=1, null=True),
        ),
    ]
