# program, który wykorzystuje listy


lista1 = [4, 6, 7, 9]
lista2 = [2, 2]
lista3 = [0]

lista1.append(lista2 * 3)   # inserts a list object
print(lista1)

lista1 = [4, 6, 7, 9]
lista1.extend(lista2 * 3)   # inserts elements of a list
print(lista1)

print(len(lista1))

lista1.sort()
print(lista1)
