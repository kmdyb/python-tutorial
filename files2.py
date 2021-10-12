# tryby otwierania plików
# r w a to tryby pojejdyncze

with open("data4", 'w') as file4:
    file4.write("bum")

with open("data4", 'a') as file4:
    file4.write("\ncyk")

with open("data4", 'a') as file4:
    file4.write("\ncyk")

# tryby mnogie pozwalają na wykonywanie kilku czynności na raz
# r+ czytanie i pisanie, jak plik nie istnieje to wyrzuca błąd :(
# w+ pisanie i czytanie rzadko używany, jak plik istnieje to kasuje jego treść :(
# a+ dopisywanie i czytanie, wiecznie dopisuje (na końcu),
#    wskaźnik przy otwarciu jest na końcu, .write() dopisuje zawsze na końcu
