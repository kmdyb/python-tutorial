# generatory są wykorzystywane do wypisywanaia, generowania na bieżąco
# nie marnuje pamięci,przerzuca pojedynczo generowane liczby

numbers = [number ** 2 for number in range(100)]    # wyrażenie listowe

numbersgenerator = (number ** 2 for number in range(100))   # generator

sum1 = sum2 = 0
for i in numbers:
    sum1 += i

for i in numbersgenerator:
    sum2 += i

print(sum1, sum2)
