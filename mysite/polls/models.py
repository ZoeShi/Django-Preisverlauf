from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

from django.utils.encoding import python_2_unicode_compatible

import datetime

from django.db import models
from django.utils import timezone


class Product(models.Model):
    Product = models.ForeignKey(
        'Product_id',
        on_delete=models.CASCADE,
        related_name='Preise',
    )
    Neuer_Preis = models.DecimalField(decimal_places=2, max_digits=10)
    Alter_Preis = models.DecimalField(decimal_places=2, max_digits=10)
    datumzeit = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.Product)


class Product_id(models.Model):
    Product = models.CharField(max_length=200)
    GuenstigsterPreis = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    AktuellerPreis = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)

    def get_absolute_url(self):
        from polls.urls import app_name
        return reverse(' % s:product' % (app_name), args=[self.pk])

    def __str__(self):
        return self.Product

    def updateGuenstigsterPreis(self):

        for i in Product.objects.filter(Product=self):
            f = []
            f.append(i.Neuer_Preis)
        self.GuenstigsterPreis = min(f)
        self.save()

        AktuellesProdukt = Product.objects.filter(Product_id=self).extra(order_by=['-datumzeit']).first()
        self.AktuellerPreis = AktuellesProdukt.Neuer_Preis
        self.save()
