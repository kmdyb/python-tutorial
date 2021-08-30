# program z zagnieżdżonymi typami danych


# lista w liście
# łatwe modyfikowanie, zasobożerne
parking1 = [
    ['Skoda Fabia', 'WX 5H6N', '15:53'],
    ['Renault Megane', 'LC 333F5', '14:21'],
    ['Dodge Chrysler', 'LU 12K9C', '15:01']
]

# krotki w liście
# Listę można modyfikować, ale krotek już nie
# zastosowanie krotek poprawia wydajność
parking2 = [
    ('Skoda Fabia', 'WX 5H6N', '15:53'),
    ('Renault Megane', 'LC 333F5', '14:21'),
    ('Dodge Chrysler', 'LU 12K9C', '15:01')
]

# krotki w zbiorze
# dzięki temu można m. in. wykonywać operacje na zbiorach: &, |, -, ^
parking3 = {
    ('Skoda Fabia', 'WX 5H6N', '15:53'),
    ('Renault Megane', 'LC 333F5', '14:21'),
    ('Dodge Chrysler', 'LU 12K9C', '15:01')
}

for model, rejestracja, czas in parking3:
    print(model)
    print(rejestracja)
    print(czas, '\n')

for wpis in parking1:
    print(wpis)
