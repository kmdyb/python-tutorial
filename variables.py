def add(c):
    c = c + 1
    print("f:", c)
    return c


c = 5
print("m:", c)
print("r:", add(c))
print("m:", c)
add(1)
print("m:", c)
add(c)
print("m:", c)
add(c)
print("m:", c)
