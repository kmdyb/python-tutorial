# program liczący pola figur

def pole_prostokata(a, b):
    # print("a * b =", a * b)
    return a * b


def pole_trapezu(a, b, h):
    return (a + b) * h / 2


def pole_trojkata(a, h):
    return a * h / 2


def pole_kwadratu(a):
    return a * a


while True:
    print("1.prostokat 2.kwadrat 3.trapez 4.trojkat 5.wyjscie")
    option = input("Podaj numer opcji: ")
    if option == '1':
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        print(pole_prostokata(a, b))
    elif option == '2':
        a = int(input("Podaj a: "))
        print(pole_kwadratu(a))
    elif option == '3':
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        h = int(input("Podaj h: "))
        print(pole_trapezu(a, b, h))
    elif option == '4':
        a = int(input("Podaj a: "))
        h = int(input("Podaj h: "))
        print(pole_trojkata(a, h))
    elif option == '5':
        break
