# program, który wykorzystuje pętle while i for
"""
i = int(input("Będę odliczać w dół. Podaj liczbę: "))

while i > 0:
    print(i)
    i -= 1

name = input("Podaj imię: ")
name = name.capitalize()

for i in name:
    print(i)

for i in range(100):
    if i % 2:
        print(i+1)
        i += 1
"""
i = suma = 0
while i < 3:
    number = int(input("Podaj dodatnią liczbę parzystą: "))
    if number > 0 and number % 2 == 0:
        suma += number
        print("Suma tych liczb wynosi", suma)
    else:
        continue
    i += 1
