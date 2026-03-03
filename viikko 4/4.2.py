while True:
    tuumat = float(input("Anna tuumamäärä (negatiivinen lukumäärä lopettaa):"))
    if tuumat < 0 :
        print("ohjelma loppu.")
        break

    senttimetrit= tuumat * 2.54
    print(f"{tuumat}tuumaa={senttimetrit}cm")