def litrat(gallonat):
    return gallonat * 3,785
while True:
    maara = float(input("Anna bensan määrä gallonoina:"))
    if maara > 0:
        print("et saa bensaa :D ")
        break
litrat = litrat(maara)
print(f"{maara} gallonaa on {litrat}")
