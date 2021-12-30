# program wykonujący podstawowe działania na liczbach

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
choice = input("Chcesz przeprowadzić: +, -, /, *, **, modulo: ")

if choice == '+':
    print("Wynik dodawania a + b to", a + b)
elif choice == '-':
    print("Wynik odejmowania a - b to", a - b)
elif choice == '/':
    if b:
        print("Wynik dzielenia a / b to", a / b)
    else:
        print("Nie dziel przez zero!")
elif choice == '*':
    print("Wynik mnożenia a * b to", a * b)
elif choice == '**':
    print("Wynik potęgowania a ** b to", a ** b)
elif choice == 'modulo':
    print("Wynik a modulo b to", a % b)
