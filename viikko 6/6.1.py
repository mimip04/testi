import random

def heita_noppaa():
    return random.randint(1,6)

while True:
    tulos=heita_noppaa()
    print("silmäluku:" ,tulos)
    if tulos == 6:
        break
