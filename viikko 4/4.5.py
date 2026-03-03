oikea_tunnus=("pyhton")
oikea_salasana=("rules")

yritykset=0


while yritykset <5:
    tunnus = input("anna käyttäjätunnus:")
    salasana = input("anna salasana:")

    if tunnus == "pyhton" and salasana == "rules":
        print("Tervetuloa!")
        break

    else:
        yritykset = yritykset+1
        print("väärä tunnus tai salasana.")

    if yritykset == 5:
        print("pääsy evätty.")




