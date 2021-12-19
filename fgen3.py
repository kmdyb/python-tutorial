def gen_cubes():
    a = 0
    while True:
        a = yield a * a


cubes = []
cube = gen_cubes()
cube.send(None)

for i in range(20, 31):
    cubes.append(cube.send(i))

print(cubes)
