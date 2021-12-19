# funkcja generuje nieskończoność przemnożonych przez siebie liczb

def gen_cubes():
    a = 1
    count = 1
    while True:
        yield count, a * a
        a += 1
        count += 1


gen = gen_cubes()
print(next(gen))
print(next(gen))
print(next(gen), "\n")

gen2 = gen_cubes()
gen2list = []


def cubes(quantity):
    print("ordered amount:", quantity)
    for i in range(quantity):
        # print(i+1, list(next(gen2)))
        gen2list.append(list(next(gen2))[1])


cubes(10)
print(gen2list)
cubes(20)
print(gen2list)
