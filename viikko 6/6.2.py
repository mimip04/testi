
import random
tahkot = int(input("Anna nopan tahkot:"))
def heita_noppaa():
    return random.randint(1,tahkot)

tulos = 0
while tulos != tahkot:
    tulos=heita_noppaa()
    print("silmäluku:" ,tulos)