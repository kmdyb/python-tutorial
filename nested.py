# program z zagnieżdżonymi typami danych


# lista w liście
# łatwe modyfikowanie, zasobożerne

# parking1 = [
#     ['Skoda Fabia', 'WX 5H6N', '15:53'],
#     ['Renault Megane', 'LC 333F5', '14:21'],
#     ['Dodge Chrysler', 'LU 12K9C', '15:01']
# ]
# for wpis in parking1:
#     print(wpis)
#
# for item in parking1:
#     for element in item:
#         print(element)
#     print()

# krotki w liście
# Listę można modyfikować, ale krotek już nie
# zastosowanie krotek poprawia wydajność
parking2 = [
    ('Skoda Fabia II', 'WX 5H6N', '15:53'),
    ('Renault Megane II', 'LC 333F5', '14:21'),
    ('Dodge Chrysler II', 'LU 12K9C', '15:01')
]

# for item in parking2:
#     for element in item:
#         print(element)
#     print()

# krotki w zbiorze
# dzięki temu można m. in. wykonywać operacje na zbiorach: &, |, -, ^
parking3 = {
    ('Skoda Fabia III', 'WX 5H6N', '15:53'),
    ('Renault Megane III', 'LC 333F5', '14:21'),
    ('Dodge Chrysler III', 'LU 12K9C', '15:01')
}
# for item in parking3:
#     for element in item:
#         print(element)
#     print()

# for model, rejestracja, czas in parking3:
#     print(model)
#     print(rejestracja)
#     print(czas, '\n')

# słownik w liście
# tutaj kolejność ma znaczenie, bardziej zasobożerne niż słownik w słowniku
# przy szukaniu jakiegoś id trzeba przejść przez wpisy aż do znalezienia go
people1 = [
    {'id': "agrsgafsd", 'name': 'Janusz', 'age': 34, 'sex': 'male'},
    {'id': "sthasdfgas", 'name': 'Kamil', 'age': 33, 'sex': 'male'},
    {'id': "asrhsbadsg", 'name': 'Julia', 'age': 36, 'sex': 'female'}
]

# for dictionary in people1:
#     for key in dictionary:
#         print(key, dictionary[key])
#     print()

# słownik w słowniku
# jest szybszy niż słownik w liście
# przy szukaniu jakiegoś id wystarczy np. people["agrsgafsd"]
people2 = {
    "agrsgafsd": {'name': 'Janusz', 'age': 34, 'sex': 'male'},
    "sthasdfgas": {'name': 'Kamil', 'age': 33, 'sex': 'male'},
    "asrhsbadsg": {'name': 'Julia', 'age': 36, 'sex': 'female'}
}
# for key in people2:
#     for key2 in people2[key]:
#         print(key2, people2[key][key2])
#     print()

# krotka w słowniku
# np. oceny uczniów
oceny = {
    "Janek": (4, 3, 5, 3, 6),
    "Ania": (5, 5, 4, 6, 4)
}
# for key in oceny:
#     print(key, oceny[key])
#     # for item in oceny[key]:
#     #     print(item)
