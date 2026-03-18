luku = []

while True:
    syote=input("anna luku (tyhjä lopettaa):")
    if syote==" ":
        break

    luku.append(float(syote))

luku.sort(reverse=True)

print("viisi suurinta lukua:")
for luku in luku [:5]:
    print(luku)

