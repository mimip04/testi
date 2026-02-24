#termejä,sisennyksiä, valintarakenne eli if lause, haarat
#sisennys neljä välilyöntiä
#ehdolliset lausekkeet, esim if
from operator import truediv
from os import times_result

raha= float(input("Kuinka paljon sinulla on rahaa?"))
if raha >= 5:
    print("voit ostaa kahvin.")

print("kiitos hei.")

#if siis joko totta tai tarua, ajetaan tai ei ajeta

#jotta voidaan verrata, onko ehto totta
#huomioi kaksi yhtäkuin merkkiä

#loogiset operaattorit
#not, and ja or,

a= True
b = False

if a and b:
    print("molemmat oli totta.")

if a or b:
    print("toinen ehto oli totta")

if not a and b:
    print("kumpikaan ei ole totta.")


#else haara

raha=float(input("Kuinka paljon sinulla on rahaa?"))

if raha >= 5:
    print("tässä kahvisi ole hyvä")

else:
    puuttuva=5-raha
    print("sorry,sinulta puuttuu",puuttuva)

print("kiitos hei")

#jos otta, ajetaan if ja jos ei ajetaan else


numero= int(input("Anna kokonaisluku:"))

if numero > 0:
    print("luku on positiivinen.")

elif numero <0:
    print("luku on negatiivinen")

else:
    print("numero oli 0.")

#jos monta vaihtoehtoa, niin elseif elif-haaroja
#elseä ei ole pakko olla, eli jos laitettaisiin 0 nii ei tulisi mitään

ika=int(input("Kuinka vanha olet?:"))

if ika>= 65:
    print("olet eläkeiässä")

elif ika >= 18:
    print("olet työikäinen.")

elif ika >= 7:
    print("olet kouluiässä")


else:
    print("olet lapsi")

#vain yksi ehto siis ajetaan

#ehtolausekkeet siäkkäin, kiinnitetään sisennykseen huomiota

numero = int(input("Anna luku:"))

if numero > 0:
    if numero % 2 == 0:
        print("numero oli parillinen")
    else:
        print("numero on pariton")

else:
    print("numero jonka annoit oli negatiivinen.")

print("jatketaan..")

