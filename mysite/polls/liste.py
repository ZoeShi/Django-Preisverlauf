import re
datei = open('Amazon_Pricing.txt')

zeilen = []
for line in datei:
    if len(line.strip()) > 0:
        zeilen.append(line.strip()) 
datei.close()

print zeilen


y = []
for i in zeilen:
    #(re.split('hat sich von', i))
    y =re.split('hat sich von', i)
    #print(y)
    d = {
        "Product": y[0],
        "Preis": y[1]
        }
    #print(d)
    d['Preis'] = re.split('auf', d['Preis'])
   # print(d)
    t = {
        "Alter Preis": d['Preis'][0],
        "Neuer Preis": d['Preis'][1]
        }
   # print(t)

    o = {
        "Product": d["Product"],
        "Alter Preis": t["Alter Preis"],
        "Neuer Preis": t["Neuer Preis"]
        }
    print(o)

