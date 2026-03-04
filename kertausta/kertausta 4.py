
tarina = " "
edellinen_sana=" "

while True:
    sana=input("Anna sana tarinaan:")

    if sana == "loppu":
        print(tarina)
        break


    if sana == edellinen_sana:
        print(tarina)
        break

    tarina += sana+" "
    edellinen_sana = sana
