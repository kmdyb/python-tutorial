# program wykonujący podstawowe działania na liczbach

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
wybor = input("Chcesz przeprowadzić: +, -, /, *, **, modulo: ")

if wybor == '+':
    print("Wynik dodawania a + b to", a + b)
elif wybor == '-':
    print("Wynik odejmowania a - b to", a - b)
elif wybor == '/':
    if b:
        print("Wynik dzielenia a / b to", a / b)
    else:
        print("Nie dziel przez zero!")
elif wybor == '*':
    print("Wynik mnożenia a * b to", a * b)
elif wybor == '**':
    print("Wynik potęgowania a ** b to", a ** b)
elif wybor == 'modulo':
    print("Wynik a modulo b to", a % b)
