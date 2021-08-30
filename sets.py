# program wykorzystujący zbiory i operacje na nich
# zbiory nie zachowują pozycji elementów


A = {43, 2, 4, 637, 2, 14}
B = {4, 2}
print('A', A)

A.add(888)
print('after A.add(888)', A)

AList = [1, 4, 3, 6, 3]
print(AList)
print(set(AList))               # zamiana listy na zbiór, usuwa elementy powtarzające się


print('A & B', A & B)                    # część wspólna zbiorów
print('A | B', A | B)                    # podaje wszystkie elementy
print('A - B', A - B)                    # podaje elementy ze zbioru A, nie będące w zbiorze B
print('B - A', B - A)                    # i na odwrót

print('A^B', A ^ B)                      # alternatywa wykluczająca, usuwa wspólne wartości

print('A', A)
A.remove(2)                     # usuwa podany element, ale wyrzuca błąd, gdy takiego brak
A.discard(2)                    # usuwa podany element i nie wyrzuca błędu, gdy takiego brak

print('A', A)
print('B', B)
A.add(2)
print('A', A)
print(A.issubset(B))                   # sprawdza podzbiorowość...
print(B.issubset(A))
