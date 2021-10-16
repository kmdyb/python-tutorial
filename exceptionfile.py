
def fileread(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File does not exist, can't read it.")


wantedFile = input("Podaj nazwę pliku: ")
print("Content:\n", fileread(wantedFile), sep="")
