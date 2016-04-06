from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, request
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render_to_response
from .forms import UploadFileForm, ProductForm, Auswahlbox
from decimal import *
from polls.models import *
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
                existing = Product.objects.filter(Product=i["Preis"])
                if len(existing) == 0:
                    k = Product()
                    k.Product = i["Preis"]
                    k.save()
                else:
                    k = existing[0]
                x = Preis()
                x.Product = k
                x.Alter_Preis = i["Alter Preis"]
                x.Neuer_Preis = i["Neuer Preis"]
                x.datumzeit = datetime.now()
                x.save()
                k.updateGuenstigsterPreis()

            return render(request, 'polls/succesurl.html')
        return render(request, 'polls/upload.html', {'form': form})

def datei(datei):


    zeilen = []
    for line in datei:
        if len(line.strip()) > 0:
            zeilen.append(str(line, 'latin-1').strip())
    datei.close()


    x = []
    for i in zeilen:
        l = re.findall(r'(.*) hat sich von EUR ([0-9]+\,[0-9]+) auf EUR ([0-9]+\,[0-9]+) .*', i)

        Preis=l[0][0]
        Alter_Preis=l[0][1].replace(",", ".")
        Neuer_Preis=l[0][2].replace(",", ".")


        o = {
       	    "Preis": Preis,
            "Alter Preis": Decimal(Alter_Preis),
            "Neuer Preis": Decimal(Neuer_Preis)
        }

        x.append(o)


    return(x)

class IndexView(generic.View):
    def get_queryset(self):
        return Product.objects.all().order_by('Product')

    def get(self,request):
        latest_Preis_list = self.get_queryset()
        form = ProductForm()
        context = {
            'latest_Preis_list': latest_Preis_list,
            'form': form
        }


        return render(request, 'polls/index.html', context)
class save2():
    def get(self, request):
        if request.method == "GET":
            req = request.GET['Kategorie']
        return render(request, 'polls/index.html')



class PreisView(generic.View):
    def get_queryset(self,pk):
        return Product.objects.filter(pk=pk)
    model = Preis
    template_name = 'polls/product.html'

    def get(self, request, pk):
        try:
            req = request.GET["Kategorie"]
            return save.button
        except:
            pass
        p = Product.objects.get(pk=pk)
        s = Preis.objects.filter(Product=pk)

        latest_Preis_list = self.get_queryset(pk=pk)

        form = ProductForm(instance=p)
        form = Auswahlbox()




        context = {
            'latest_Preis_list': latest_Preis_list,
            's': s,
            'form': form,
            'p': p,
        }
        return render(request, 'polls/product.html', context)




class PreisCSVView(generic.View):
    def get(self, request, pk):

        p = Product.objects.get(pk=pk)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)
        writer.writerow(['Zeit', 'Preis'])
        all_Preis_prices = Preis.objects.filter(Product=p).extra(order_by=['datumzeit'])

        count = 0
        checker_neu = None
        checker_alt = None




        for prc in all_Preis_prices:
            if checker_neu is not None and checker_alt is not None:
                if prc.Alter_Preis == prc.Neuer_Preis:
                    writer.writerow([count, str(prc.Alter_Preis)])
                    continue
                elif checker_neu == prc.Alter_Preis:
                    checker_alt = prc.Alter_Preis
                    checker_neu = prc.Neuer_Preis

                    writer.writerow([count, str(prc.Alter_Preis)])
                    count += 1
                    writer.writerow([count, str(prc.Neuer_Preis)])
                elif checker_neu == prc.Neuer_Preis:
                    checker_alt = prc.Alter_Preis
                    checker_neu = prc.Neuer_Preis

                    writer.writerow([count, str(prc.Neuer_Preis)])
                    count += 1
                    writer.writerow([count, str(prc.Neuer_Preis)])
                elif checker_alt == prc.Neuer_Preis:
                    writer.writerow([count, str(prc.Neuer_Preis)])
                elif checker_neu != prc.Alter_Preis:
                    writer.writerow([count, str(prc.Neuer_Preis)])
                    writer.writerow([count, str(checker_neu)])
                elif prc.Alter_Preis != prc.Neuer_Preis:
                    writer.writerow([count, str(prc.Neuer_Preis)])
                    writer.writerow([count, str(prc.Alter.preis)])
                elif checker_neu != prc.Neuer_Preis:
                    writer.writerow([count, str(prc.Neuer_Preis)])
                    writer.writerow([count, str(checker_neu)])
                elif checker_alt != checker_neu:
                    writer.writerow([count, str(checker_alt)])
                    writer.writerow([count, str(checker_neu)])
                elif checker_alt != prc.Neuer_Preis:
                    writer.writerow([count, str(checker_alt)])
                    writer.writerow([count, str(prc.Neuer_Preis)])

            else:
                checker_alt = prc.Alter_Preis
                checker_neu = prc.Neuer_Preis

                writer.writerow([count, str(prc.Alter_Preis)])
                count += 1
                writer.writerow([count, str(prc.Neuer_Preis)])

        return response


class search(generic.View):

    def get(self,request):
        search_query = request.GET.get('search_box', None)
        gesuchtesproduct = Preis.objects.filter(Product__contains=search_query)
        form = UploadFileForm()
        context = {
            'latest_Preis_list': gesuchtesproduct,
            'form': form
        }
        return render(request, 'polls/index.html', context)



