from django.db import models
from django_countries.fields import CountryField

class Brand(models.Model):
    """
    Creation of model Brand
    """
    name = models.CharField(max_length=60, verbose_name="Name of the Brand", unique=True)
    founder = models.CharField(max_length=60, verbose_name="Founder")
    country = CountryField(blank_label='(select country)')
    logo = models.ImageField(upload_to='tablets/static/pictures', default='logo')

    def __str__(self):
        return self.name

class Tablet(models.Model):
    """
    Creation of model Tablet
    """
    name = models.CharField(max_length=60, verbose_name="Name of the Tablet", unique=True)
    description = models.TextField(verbose_name="Description of the Tablet", blank = True)
    brand = models.ForeignKey(Brand, default="", verbose_name="Brand", on_delete=models.PROTECT, related_name="b_tablet")
    storage_size = models.FloatField(verbose_name="Storage size en Gigabytes (Gb)", null=True)
    release_year = models.IntegerField(verbose_name="Release year", null=True)
    picture = models.ImageField(upload_to='tablets/static/pictures')

    def __str__(self):
        return self.name