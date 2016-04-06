from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

from django.utils.encoding import python_2_unicode_compatible

import datetime

from django.db import models
from django.utils import timezone


class Preis(models.Model):
    Product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    Neuer_Preis = models.DecimalField(decimal_places=2,max_digits=10)
    Alter_Preis = models.DecimalField(decimal_places=2,max_digits=10)
    datumzeit = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return str(self.Product)


class  Product(models.Model):
    Kategorie_Choices = (
        ('Blu-Ray', 'Blu-Ray'),
        ('Geschirr', 'Geschirr'),
        ('DVD', 'DVD')
    )
    Product = models.CharField(max_length=1000)
    GuenstigsterPreis = models.DecimalField(decimal_places=2,max_digits=10,default=0.0)
    AktuellerPreis = models.DecimalField(decimal_places=2,max_digits=10,default=0.0)
    Kategorie = models.CharField(max_length=400, choices=Kategorie_Choices)
    def get_absolute_url(self):
        from polls.urls import app_name
        return reverse('%s:product'%(app_name), args=[self.pk])

    def __str__(self):
        return self.Product

    def updateGuenstigsterPreis(self):

        for i in Preis.objects.filter(Product=self):
            f = []
            f.append(i.Neuer_Preis)
        self.GuenstigsterPreis = min(f)
        self.save()

        AktuellesProdukt = Preis.objects.filter(Product=self).extra(order_by=['-datumzeit']).first()
        self.AktuellerPreis = AktuellesProdukt.Neuer_Preis
        self.save()





