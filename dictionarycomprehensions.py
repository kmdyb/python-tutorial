# wyrażenia słownikowe
# lista imion i wyrażenie słownikowe z ich długością
names = ["Ania", "Bob", "Jan", "Ola", "Irek", "Joe"]
names2 = {
    name: len(name)
    for name in names
}
print("imiona i ich długość", names2)

# lista liczb i wyrażenie słownikowe z ich kwadratem
numbers = [2, 5, 324, 3, 231, 36, 72]
numbers2 = {
    number: number ** 2
    for number in numbers
}
print("liczby i ich kwadraty", numbers2)

# celsjusz do fahrenheit
celcius = {"t1": -4, "t2": 32, "t3": 235, "t4": 82, "t5": -46, "t6": -16, "t7": 90, "t8": 11, "t9": 0}

fahrenheit = {
    index: temp * 1.8 + 32
    for index, temp in celcius.items()
}
print(fahrenheit)
