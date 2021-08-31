# program wykorzystujący słowniki {klucz: wartość}
# kolejność w słownikach nie ma znaczenia
# każdy klucz występuje tylko raz (kolejne jego zdefiniowanie nadpisuje poprzednie)

# przy definiowaniu słownika, brane są wartości, a nie adresy (odnośnie języka C)
a, b, c, d = 1, 2, 3, 4
dict1 = {a: b, c: d, 4: 5}
print(dict1)
a = 2
print(dict1)

# jednak można je zmieniać
dict1[a] = 0  # dodaje na końcu klucz 2 (aktualna wartość a) oraz wartość 0
print(dict1)
dict1[1] = 0  # zmienia wartość klucza 1
print(dict1)

dict1.update({1: 666})  # metoda update() zmienia wartosć
print(dict1)
dict1.update({11: 666})  # metoda update() dodaje klucz i wartość
print(dict1)

dict2 = {555: 555}  # metoda update() dodaje inny słownik
dict1.update(dict2)
print(dict1)

# metody usuwania kluczy
del (dict1[1])
print(dict1)

print('usuwam: ', dict1.pop(3))  # metoda pop() zwraca wartość usuniętego klucza
print(dict1)

print('usuwam: ', dict1.popitem())  # metoda popitem() usuwa ostatni element i zwraca ... coś
print(dict1)
print(type(dict1.popitem()))  # zwraca krotkę

print('długość dict1:', len(dict1))

dict1.clear()
print('po metodzie clear, wypisuję dict1: ', dict1)

parking = {
    34: 'Renault Megane',
    55: 'Skoda Fabia',
    11: 'Jeep Cheeroke'
}
print(parking.get(34))
print(parking.get(35))


def parkingcheck(spaceid):
    return "Na tym miejscu %s." % parking.get(spaceid, "nic nie stoi, możesz parkować")


print(parkingcheck(34))
print(parkingcheck(35))
