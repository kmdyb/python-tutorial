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


def finish_timer(starttimer):
    endtimer = time.perf_counter()
    return endtimer - starttimer


def function_performance(func, arg):
    starttimer = time.perf_counter()
    print(func(arg))
    endtimer = time.perf_counter()
    return endtimer - starttimer


start = time.perf_counter()
print(sumuj_do(111))
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
print(sumuj_do2(111))
print(time.perf_counter() - start)

start = time.perf_counter()
print(sumuj_do3(111))
print(finish_timer(start))

print(function_performance(sumuj_do4, 111))

print(function_performance(sumuj_do5, 111))
