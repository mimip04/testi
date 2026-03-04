while True:
    print("1=summa, 2=erotus, 3=tulo, 4=osamäärä, 5=lopeta")
    toiminto=input("valitse toiminto")
    if toiminto == "5":
        print("loppu")
        break



    luku1= float(input("valitse luku1"))
    luku2= float(input("valitse luku2"))

    if toiminto == "1":
        print("tulos: ", luku1+luku2)
    elif toiminto == "2":
        print("tulos: ", luku1-luku2)
    elif toiminto == "3":
        print("tulos: ", luku1*luku2)
    elif toiminto == "4":
        if luku2==0:
            print("nollalla ei voida jakaa.")
        else:
            print("tulos: ", luku1/luku2)

    else:
        print("virheellinen valinta")

