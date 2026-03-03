import random

N = int(input("kuinka monta pistettä arvotaan?"))

n = 0

for i in range(N):
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

    if x*x + y*y < 1:
        n = n+1

pi_likiarvo = 4*n/N
print("piin likiarvo on:", pi_likiarvo)


