#loop, miten toimii
#while-toistorakenne = ehdollinnen ja yksinkertainen
#break lauseke, continuea lauseke

hinta=5
rahaa_annettu=0

#ehto, ehdon päivitys
while rahaa_annettu<hinta:
    rahaa_annettu+=1
    print("rahaa annettu", rahaa_annettu)

print("kahvi maksettu.")

#sama esim. yksinkertainen

while True:
    rahaa_annettu+=1
    print("rahaa annettu", rahaa_annettu)

    if rahaa_annettu==hinta:
        break

    print("anna lisää rahaa")  #break jälkeen ei ajeta mitään


print("kahvi maksettu.")



# ei käsky

kasky=input("annetaanko lisää rahaa (ei lopettaa) ?")
while kasky != "ei":
    print("annettu kolikko lisää")
    kasky = input("annetaanko lisää rahaa?")

print("ohjelma päättyy.")

#infinite loop

