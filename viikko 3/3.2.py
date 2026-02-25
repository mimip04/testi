hytti= input("anna hyttiluokka (lux, a, b, c):").upper()


if hytti == "lux":
    print("lux on parvekkeellinen hytti")

elif hytti == "a":
    print("a on autakannen alapuolella")

elif hytti == "b":
    print("b on ikkunaton")

elif hytti == "c":
    print("c on ikkunaton atuokannen alapuolella")

else:
    print("virheellinen luokka")
