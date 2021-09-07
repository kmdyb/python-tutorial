# wyrażenia zbiorów

names = {"Anna", "grzesiek", "Bartek", "Ola", "beata"}

names2 = {
    name.capitalize()
    for name in names
    if name[0] != ('g' or 'G')
}
print(names2)
