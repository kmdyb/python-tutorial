# funkcje generujące
# yield (dostarczyć, wydać), send
# generatory służą do generowania na bieżąco, kiedy zachodzi potrzeba

evenNumberGenerator = {
    element
    for element in range(100)
    if element % 2 == 0
}
#  chcemy zrobić coś takiego


def generate_even_numbers():
    for element in range(100):
        if element % 2 == 0:
            return element
# zwraca pierwszy pasujący element i na tym koniec funkcji


def generate_even_numbers2():
    print("start")
    for element in range(100):
        print("przed yield")
        if element % 2 == 0:
            yield element
            print("po yield")
# zwraca pasujący element i czeka na kolejne wywołanie


a = generate_even_numbers()     # zwykłe wywołanie i przypisanie wyniku do zmiennej
a2 = generate_even_numbers2()   # stworzyliśmy generator i przypisaliśmy go do zmiennej

print("a2:", a2)
print("przed nextami")
print("next(a2):", next(a2))    # zwraca element i czeka
print("między dwoma nextami")
print("next(a2):", next(a2))    # wraca do pętli w to samo miejsce i kontynuuje
print("koniec nextów\n")
# ------------------------------


def generate_10_numbers():
    x = 0
    while x < 10:
        yield x
        x = x + 1


print("1", list(generate_10_numbers()))
print("2", list(generate_10_numbers()))
liczby = generate_10_numbers()
print("3", next(liczby))
print("3", next(liczby))
print("3", next(liczby))

generate_10_numbers_expression = {x
                                  for x in range(10)}
print("4", list(generate_10_numbers_expression))
print("5", list(generate_10_numbers_expression))

print("6", {x for x in range(10)})
print("7", list({x for x in range(10)}))
