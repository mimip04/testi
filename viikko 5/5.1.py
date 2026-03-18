import random

arpakuutio = int(input("anna arpakuutioiden lukumäärä:"))

summa=0

for i in range(arpakuutio):
    heitto= random.randint(1,6)
    summa += heitto

print("silmälukujen summa on:",summa)
