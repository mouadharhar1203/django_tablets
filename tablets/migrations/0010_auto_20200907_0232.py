# Generated by Django 3.1.1 on 2020-09-07 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablets', '0009_auto_20200907_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=60, unique=True, verbose_name='Name of the Tablet'),
        ),
    ]