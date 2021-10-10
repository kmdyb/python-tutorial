#   --------------- operacje na pliku
plik = open("data", "w")  # handle
plik.write("test data1")
plik.write("test data2")
plik.close()
#   --------------- konstrukcja try ... finally
try:
    print("test try before")
#    print(0/0)     # optional comment
    print("test try after")
finally:
    print("finally text")
#   --------------- konstrukcja with ... as
with open("data2", "w") as pliczek2:    # handle
    pliczek2.write("test with as before ")
#    print(0 / 0)   # optional comment
    pliczek2.write("test with as after")
# pliczek2.write("test with as out of scope")       # optional comment

#   --------------- .read()
with open("data3", "r", encoding="UTF-8") as file3:
    fromfile = file3.read()
    print("from file\n", fromfile)
    print("2nd from file\n", fromfile)
    print(file3.read())
# można użyć .read() tylko raz?
    print(fromfile.splitlines())
# poniższe .readline() też nie zadziała, bo już była użyta metoda .read()
    linia1 = file3.readline()
    linia2 = file3.readline()
    linia3 = file3.readline()
    print(linia1, linia2, linia3)
# poniższe readlines() odczyta linie i wrzuci je w listę (wraz z \n)
    file3.readlines()
# żeby nie było znaków nowej linii \n najlepiej wykorzystać poniższe
    file3.read().splitlines()
# można też tak, ale to i tak nie będzie wykonane, bo plik był odczytany
    for line in file3:
        print(line)
