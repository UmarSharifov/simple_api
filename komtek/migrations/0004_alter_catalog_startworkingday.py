# Generated by Django 3.2.4 on 2021-06-25 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('komtek', '0003_auto_20210625_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='StartWorkingDay',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]