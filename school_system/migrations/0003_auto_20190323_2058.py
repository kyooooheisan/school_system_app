# Generated by Django 2.0.13 on 2019-03-23 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_system', '0002_lessonrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonrecord',
            name='lesson_day',
            field=models.DateField(verbose_name='受講日'),
        ),
    ]
