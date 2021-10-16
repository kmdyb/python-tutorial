lista = []

with open("imiona.txt", "r", encoding="UTF-8") as file:
    for line in file:
        lista.append(tuple(line.replace("\n", "").split(" ")))
print(lista)


with open("imiona2.txt", "w", encoding="UTF-8") as file:
    for item in lista:
        file.write(item[0] + "\n")

with open("nazwiska.txt", "w", encoding="UTF-8") as file:
    for item in lista:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")
""" poniżej słabsze, nieczytelne
        if len(item) == 2:
            file.write(item[1] + "\n")
        else:
            file.write("\n")
"""