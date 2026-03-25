
luvut = list(range(1, 20))
def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

tulos = laske_summa(luvut)
print("listan lukujen summa:", tulos)