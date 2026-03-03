import random
luku= random.randint(1,10)

while True:
    arvaus=int(input("Arvaa luku väliltä 1-10:"))

    if arvaus > luku:
        print("liian suuri arvaus")

    elif arvaus < luku:
        print("liian pieni arvaus")

    else:
        print("oikea luku!")
        break


