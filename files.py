"""#   --------------- operacje na pliku
file1 = open("data", "w")  # handle
file1.write("test data1")
file1.write("test data2")
file1.close()
"""

"""#   --------------- konstrukcja try ... finally
try:
    print("test try before")
#    print(0/0)
    print("test try after")
finally:
    print("finally text")
"""

"""#   --------------- konstrukcja with ... as
with open("data2", "w") as file2:    # handle
    file2.write("test with as before ")
#    print(0 / 0)
    file2.write("test with as after")
# file2.write("test with as out of scope")       # won't work as the file's been closed
"""

#   --------------- .read()
with open("data3", "r", encoding="UTF-8") as file3:
    print("printing file3.read():")
    print(file3.read())

    file3.seek(0)
    fromfile = file3.read()
    print("\nprinting object created from file3.read():\n", fromfile)

    file3.seek(0)
    print("\nprinting file3.readlines(): ", file3.readlines())

    print("printing fromfile.splitlines():", fromfile.splitlines())

    file3.seek(0)
    print("printing file3.read().splitlines() after file3.seek(0) of course:", file3.read().splitlines())

    file3.seek(0)
    print()
    print(linia1 := file3.readline(), file3.tell())
    print(linia2 := file3.readline(), file3.tell())
    print(linia3 := file3.readline(), file3.tell())
    print(linia1, linia2, linia3, sep='')

    file3.seek(0)
    for line in file3:
        print(line, end='')
    print()
