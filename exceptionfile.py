
def fileread(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File does not exist, can't read it.")


print(fileread("data"))
