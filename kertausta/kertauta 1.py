from selectors import SelectSelector

nimi = input("Kerro nimesi:")

if nimi != "matti":
    maara=int(input("Kuinka monta keittoannosta haluat?:"))
    hinta= maara * 5.90
    print("kokonaishinta on:",hinta)


print("seuraava kiitos!")

