def suurin_arvo(a,b,c):
    return max(a,b,c)


arvo1 = int(input("Anna arvo 1: "))
arvo2 = int(input("Anna arvo 2: "))
arvo3 = int(input("Anna arvo 3: "))

suurin = suurin_arvo(arvo1,arvo2,arvo3)
print("suurin arvo on:", suurin)