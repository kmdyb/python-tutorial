# program wykorzystujący wyrażenia listowe


# potęgi liczb na dwa sposoby
liczby1 = []
for i in range(11):
    liczby1.append(i ** 2)
print(liczby1)

liczby2 = [i ** 2 for i in range(11)]
print(liczby2)

# liczby parzyste
liczby3 = []
for i in range(11):
    if i % 2 == 0:
        liczby3.append(i)
print(liczby3)

liczby4 = [i for i in range(11) if i % 2 == 0]
print(liczby4)

# test z range()
print([i for i in range(11)])
print([i for i in range(1, 11)])
print([i for i in range(1, 11, 2)])
print([i for i in range(0, 11, 2)])
