# Generated by Django 3.1.1 on 2020-09-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablets', '0006_auto_20200905_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablet',
            name='picture',
            field=models.ImageField(blank=True, upload_to='tablets/static/pictures'),
        ),
    ]
