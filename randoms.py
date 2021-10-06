# testing random
import random
from collections import Counter


def randomfunc():
    a = random.random()
    print(a, end=', ')
    print(int(a * 10), end='; ')
    return int(a * 10)


list1 = []
x = 0
while x < 10:
    list1.append(random.randint(1, 9))
    x = x + 1
print(list1, end=', ')
print(Counter(list1), "\n")


list2 = []
x = 0
while x < 10:
    list2.append(randomfunc())
    x = x + 1
print(list2)
print(Counter(list2), "\n")

# ---------

listaimion = ["ana", "bob", "joe", "max", "joe", "joe"]

print((random.choice(listaimion)))

print((random.choices(listaimion, k=10)))   # podajemy listę, listę z mnożnikami oraz ilość losowań
print(Counter(random.choices(listaimion, [1, 1, 1, 1, 1, 10], k=1000)))

print("\n", listaimion, sep='')
random.shuffle(listaimion)          # zastosowanie np. tasowanie talii kart
print(listaimion, "\n")
# a do rozdawania najlepiej pasuje pop()

print(random.sample(range(50), 6))  # wybiera 6 unikalnych liczb (elementów z podanego obiektu)
# a na piechotę to tak
koszyk = []
while len(koszyk) < 6:
    los = random.randint(1, 49)
    if los not in koszyk:
        koszyk.append(los)
print(koszyk, "\n")

print(random.sample(listaimion, 2))     # unikalne elementy (powtórzone imiona mogą się powtórzyć)
