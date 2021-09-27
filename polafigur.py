# program liczący pola figur

from enum import IntEnum


def pole_prostokata(a, b):
    # print("a * b =", a * b)
    return a * b


def pole_trapezu(a, b, h):
    return (a + b) * h / 2


def pole_trojkata(a, h):
    return a * h / 2


def pole_kwadratu(a):
    return a * a


Menu_Figures = IntEnum('Menu_Figures', 'Prostokąt Kwadrat Trapez Trójkąt Wyjście')

while True:
    print("1.prostokat 2.kwadrat 3.trapez 4.trojkat 5.wyjscie")
    option = int(input("Podaj numer opcji: "))
    if option == Menu_Figures.Prostokąt:
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        print(pole_prostokata(a, b))
    elif option == Menu_Figures.Kwadrat:
        a = int(input("Podaj a: "))
        print(pole_kwadratu(a))
    elif option == Menu_Figures.Trapez:
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        h = int(input("Podaj h: "))
        print(pole_trapezu(a, b, h))
    elif option == Menu_Figures.Trójkąt:
        a = int(input("Podaj a: "))
        h = int(input("Podaj h: "))
        print(pole_trojkata(a, h))
    elif option == Menu_Figures.Wyjście:
        break
