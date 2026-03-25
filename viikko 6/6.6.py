import math

def pizza_hinta(halkaisija, hinta):
    sade_m = (halkaisija / 2)/100
    pinta_ala = math.pi * sade_m ** 2
    return hinta / pinta_ala

halkaisija1 = float(input("Anna ensimmäisen pitsan halkaisija (cm):"))
hinta1 = float(input("Anna ensimäisen pitsan hinta (e):"))

halkaisija2 = float(input("Anna toisen pitsan halkaisija (cm):"))
hinta2 = float(input("anna toisen pitsan hinta (e):"))

eka_hinta = pizza_hinta(halkaisija1, hinta1)
toka_hinta = pizza_hinta(halkaisija2, hinta2)

print(f"ensimmäisen pitsan yksikköhinta: {eka_hinta:.2f} e/m2")
print(f"toisen pitsan yksikköhinta: {toka_hinta:.2f} e/m2")

if eka_hinta < toka_hinta:
    print("ensimmäinen pitsa on parempi valinta.")
elif toka_hinta < eka_hinta:
    print("toine pitsa on parempi valinta.")
else:
    print("molemmat ovat hyviä valintoja.")