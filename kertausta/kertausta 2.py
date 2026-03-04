tuntipalkka=float(input("Anna tuntipalkka:"))
tehdyt_tunnit=float(input("Anna tehdyt_tunnit:"))
viikonpaiva=input("Anna viikonpäivä:")
paivapalkka= tuntipalkka*tehdyt_tunnit


if viikonpaiva == "sunnuntai":
    print("päiväpalkka",tuntipalkka*tehdyt_tunnit*2)

else:
    print("päiväpalkka:", paivapalkka)



