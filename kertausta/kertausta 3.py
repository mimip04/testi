

from math import sqrt

while True:
    luku = int(input("Anna kokonaisluku:"))
    if luku < 0:
        print("virheellinen numero")
    elif luku > 0:
        print(sqrt(luku))

    else:
        print("kiinnostavaa..")
