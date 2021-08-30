# program liczący wartość bezwzględną

a = int(input("Podaj liczbę, z której chcesz uzyskać liczbę bezwzględną: "))
if a < 0:
    b = abs(a)
else:
    b = a
print("Wartość bezwzględna z liczby", a, "jest równa", b)
