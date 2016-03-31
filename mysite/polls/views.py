from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .forms import UploadFileForm, Product_idForm
from decimal import *
from polls.models import Product, Product_id
from datetime import datetime

import re
import csv

class UploadView(generic.View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'polls/upload.html', {'form': form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #datei(request.FILES['file'])
            for i in datei(request.FILES['file']):
                existing = Product_id.objects.filter(Product=i["Product"])
                if len(existing) == 0:
                    k = Product_id()
                    k.Product = i["Product"]
                    k.save()
                else:
                    k = existing[0]
                x = Product()
                x.Product = k
                x.Alter_Preis = i["Alter Preis"]
                x.Neuer_Preis = i["Neuer Preis"]
                x.datumzeit = datetime.now()
                x.save()
                k.updateGuenstigsterPreis()

            return render(request, 'polls/succesurl.html')
        return render(request, 'polls/upload.html', {'form': form})

def datei(datei):
    #datei = open('Amazon_Pricing.txt')

    zeilen = []
    for line in datei:
        if len(line.strip()) > 0:
            zeilen.append(str(line, 'latin-1').strip())
    datei.close()

    y = []
    x = []
    for i in zeilen:
        l = re.findall(r'(.*) hat sich von EUR ([0-9]+\,[0-9]+) auf EUR ([0-9]+\,[0-9]+) .*', i)


        Product=l[0][0]
        Alter_Preis=l[0][1].replace(",", ".")
        Neuer_Preis=l[0][2].replace(",", ".")

        o = {
       	    "Product": Product,
            "Alter Preis": Decimal(Alter_Preis),
            "Neuer Preis": Decimal(Neuer_Preis)
        }

        x.append(o)

    return(x)

class IndexView(generic.View):
    def get_queryset(self):
        return Product_id.objects.all()

    def get(self,request):
        latest_Product_list = self.get_queryset()
        form = UploadFileForm()
        context = {
            'latest_Product_list': latest_Product_list,
            'form': form
        }

        return render(request, 'polls/index.html', context)




class ProductView(generic.View):
    model = Product
    template_name = 'polls/product.html'

    def get(self, request, pk):
        p = Product_id.objects.get(pk=pk)
        form = Product_idForm(instance=p )



        context = {
            'form': form,
        }
        return render(request, 'polls/product.html', context)

class ProductCSVView(generic.View):
    def get(self, request, pk):
        p = Product_id.objects.get(pk=pk)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)
        writer.writerow(['Zeit', 'Preis'])
        all_product_prices = Product.objects.filter(Product=p).extra(order_by=['datumzeit'])

        count = 0
        for prc in all_product_prices:
            writer.writerow([count, str(prc.Alter_Preis)])
            writer.writerow([count + 1, str(prc.Neuer_Preis)])
            count += 2
        return response



