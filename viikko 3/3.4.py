vuosi=int(input("Anna vuosiluku jonka haluat tarkistaa:"))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("vuosi on karkausvuosi")

else:
    print("vuosi ei ole karkausvuosi")

#taii

if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
        print("vuosi on karkausvuosi")
    else:
        print("vuosi ei ole karkausvuosi")
else: print("ei ole karkausvuosi")