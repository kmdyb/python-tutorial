# user can add new definitions
# search for existing definitions
# and delete chosen definitions

dictionary = {}


def dodaj(key, definition):
    if key in dictionary:
        print("Takie hasło już istnieje.")
    else:
        dictionary[key] = definition
        print("Hasło dodane do słownika.")


def znajdz(key):
    if key in dictionary:
        print("Znalazłem hasło.", key, "oznacza", dictionary[key])
    else:
        print("Nie znalazłem hasła.")


def usun(key):
    if key in dictionary:
        del dictionary[key]
    else:
        print("Nie znalazłem hasła.")


def wypisz():
    print("Aktualny stan słownika:", dictionary)



while(True):
    print("1. Dodanie wpisu\n2. Szukanie wpisu\n3. Usuwanie wpisu\n4. Wypisz słownik\n5. Zakończ program")
    wybor = input("Co chcesz zrobić? ")
    if wybor == '1':
        dodaj(input("Podaj hasło: "), input("Podaj definicję: "))
    elif wybor == '2':
        znajdz(input("Podaj hasło: "))
    elif wybor == '3':
        usun(input("Podaj hasło: "))
    elif wybor == '4':
        wypisz()
    elif wybor == '5':
        print("Narazie.")
        break
