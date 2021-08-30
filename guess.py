# program, który polega na zgadywaniu liczby

luckynumber = 66
guess = int(input("Podaj liczbę: "))

while guess != luckynumber:
    if guess > luckynumber:
        print("za duża")
    elif guess < luckynumber:
        print("za mała")
    else:
        break
    guess = int(input("Podaj liczbę: "))

print("Gratulacje!")
