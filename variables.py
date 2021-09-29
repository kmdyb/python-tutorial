def add(c):
    c = c + 1
    print("f:", c)
    return c


# local vs global variables
"""
c = 5
print("m:", c)
print("r:", add(c))
print("m:", c)
add(1)
print("m:", c)
add(c)
print("m:", c)
add(c)
print("m:", c)
"""
# mutable vs immutable variables

# obiekty zmienne (mutable) ...
listSample = [1, 5, 62, 8]
listSample2 = listSample
listSample2.append(666)
print(listSample, "----", listSample2)
print(id(listSample), "---", id(listSample2))
# ... są powiązane, wskazują na to samo miejsce w pamięci

# obiekty niezmienne (immutable): bool, int, float, tuple, str ...
a = 4
b = a
b = 7
print("a:", a, " --- b:", b)
print(id(a), "---", id(b))
# ... mają gwarantowaną wartość, nie zmieniają się przy ich przypisywaniu do innego obiektu
# znak '=' wskazuje na nowy obiekt, tworzy nowe powiązanie


# ciekawostka
h = 4
k = 4
print("h:", h, " --- k:", k)
print(id(h), "---", id(k))
# powodem jest optymalizacja, czwórka jest jednym obiektem
print("funkcja add2")
c2 = 5
print(id(c2))


def add2(c2, amount=1):
    print(id(c2))
    c2 = c2 + amount
    print(id(c2))


add2(c2)
# tutaj na początku zmienna lokalna ma taki sam adres jak globalna, bo ma taką samą wartość


def append_to_list(lista, element):
    print(id(lista))
    lista.append(element)
    print(id(lista))


print("funkcja append")
print(id(listSample))
append_to_list(listSample, 5)
# lista jest obiektem zmiennym, więc adres jest wszędzie ten sam
