# podwajamy liczby


def double(x):
    return x * 2


# tradycyjnie
a = 3
print(double(a))

# koślawo, bo lambda to ułatwienie gdy nie chcemy przypisywać nazwy dla jednorazowej funkcji
funcinobj = lambda b: b * 2
print(funcinobj(3))

# tak najlepiej
print((lambda c: c * 2)(3))


# inne zastosowanie, filtrujemy
list1 = [4, 7, 1, 46, 8, 2]
print("\n", list1, sep='')
filteredlist = list(filter(lambda d: d % 2 == 0, list1))        # filter() potrzebuje funkcji na pierwszym argumencie
print(filteredlist)

# chociaż lepiej to zrobić wyrażeniem listowym
filteredlist2 = [e for e in list1 if e % 2 == 0]
print(filteredlist2)
