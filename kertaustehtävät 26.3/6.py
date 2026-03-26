print("TERVETULOA KÄYTTÄMÄÄN LASKINTA!")

def yhteenlasku(a,b):
    return a + b

def vahennus(a,b):
    return a - b

def kertolasku(a,b):
    return a * b

def jakolasku(a,b):
    if b == 0:
        return "nollalla ei voi jakaa."
    return a / b

while True:
    print("\nValitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku \n C: Kertolasku"
          "\n D: Jakolasku")

    valinta = input("Valintasi (A-D, Q lopettaa): ")

    if valinta == "Q":
        print("Ohjelma lopetetaan.")
        break

    a = float(input("Anna eka luku: "))
    b = float(input("Anna toka luku: "))

    if valinta == "A":
        print("Lukujen summa on:", yhteenlasku (a,b))
    elif valinta == "B":
        print("Lukujen erotus on:", vahennus (a,b))
    elif valinta == "C":
        print("Lukujen tulo on:", kertolasku (a,b))
    elif valinta == "D":
        print("Lukujen osamäärä on:", jakolasku (a,b))
    else:
        print("Virheellinen valinta tai luku.")

