# wykorzystywane są do wypisywanaia, generowania na bieżąco
# nie marnuje pamięci

numbers = [number ** 2 for number in range(100)]    # wyrażenie listowe

numbersgenerator = (number ** 2 for number in range(100))

sum1 = sum2 = 0
for i in numbers:
    sum1 += i

for i in numbersgenerator:
    sum2 += i

print(sum1, sum2)
