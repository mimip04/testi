#Kirjoita ohjelma lentoasematietojen hakemiseksi ja
# tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä
# syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai
# lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos
# käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan
# lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
# ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten
# monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät
# koodeja helposti selaimen avulla.)


lentoasemat = {}

while True:
    print("valitse toiminto:")
    print("1 = syötä uusi lentoasema:")
    print("2 = Hae lentoasema")
    print("0 = lopeta")

    valinta = input("valintasi: ")

    if valinta == "0":
        print("ohjelma lopetetaan.")
        break

    elif valinta == "1":
        icao = input("anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("anna haettava ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"lentoaseman nimi on: {lentoasemat[icao]}")
        else :
            print("lentoasemaa ei löytynyt.")

    else:
        print("virheellinen valinta.")





