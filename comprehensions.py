# ćwiczenie polegające na znalezieniu liczb
# z zakresu podzielnych przez 7 i niepodzielnych przez 5

numbers = (
    number
    for number in range(1, 471)
    if (number % 7 == 0)
    if (number % 5 != 0)
)

for i in numbers:
    print(i)
