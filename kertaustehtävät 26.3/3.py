lista = ["maito", "kananmuna", "suklaa", "karkki", "piimä", "jauho"]

laskuri = 0

for sana in lista:
    if len(sana) > 5:
        laskuri +=1

print("yli viisi kirjainta sisältävät sanat:", laskuri)