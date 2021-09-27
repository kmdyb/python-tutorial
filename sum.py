# program liczący sumę liczb od 1 do podanej

import time


def sumuj_do(liczba):
    suma = 0

    for liczba in range(1, liczba + 1):
        suma = suma + liczba
    return suma


def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])


def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1, liczba + 1)})


def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1, liczba + 1)))


def sumuj_do5(liczba):
    return int((1 + liczba) / 2 * liczba)


start = time.perf_counter()
print(sumuj_do(11))
print(time.perf_counter() - start)

print(sumuj_do2(11))
print(sumuj_do3(11))
print(sumuj_do4(11))
print(sumuj_do5(11))
