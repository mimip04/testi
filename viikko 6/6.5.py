
luvut = list(range(1, 20))
def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

def karsittu_lista(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

karsittu = karsittu_lista(luvut)
tulos = laske_summa(luvut)
print("alkuperäinen lista:", luvut)
print("pariton lista:", karsittu)