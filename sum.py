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


def function_performance(func, arg, f_iterations=1):
    sumtimer = 0
    print("Calculated value:", func(arg), "     Time elapsed:", end=' ')
    for i in range(0, f_iterations):
        starttimer = time.perf_counter()
        func(arg)
        endtimer = time.perf_counter()
        sumtimer = sumtimer + endtimer - starttimer
    return sumtimer


"""
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
"""
tested_value = 111
iterations = 1
print(function_performance(sumuj_do, tested_value, iterations))
print(function_performance(sumuj_do2, tested_value, iterations))
print(function_performance(sumuj_do3, tested_value, iterations))
print(function_performance(sumuj_do4, tested_value, iterations))
print(function_performance(sumuj_do5, tested_value, iterations))
