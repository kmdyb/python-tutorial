import copy
# do opisania, poprawienia


def listfunction2(somelist):
    print("infunc before elements  ", somelist, somelist[0], somelist[0][0], sep='      ')
    print("infunc before ids        ", id(somelist), id(somelist[0]), id(somelist[0][0]), sep='     ')
    somelist[0][0] = 2
    print("infunc after ids         ", id(somelist), id(somelist[0]), id(somelist[0][0]), sep='     ')
    print("infunc after elements   ", somelist, somelist[0], somelist[0][0], sep='      ')


list2 = [[1, 3], [5, 3], [7, 2]]
print("using listfunction2(list2[:])")
print("outer before elements   ", list2, list2[0], list2[0][0], sep='      ')
print("outer before ids         ", id(list2), id(list2[0]), id(list2[0][0]), sep='     ')
listfunction2(list2[:])      # creates a (shallow) copy to work on
print("outer after elements    ", list2, list2[0], list2[0][0], sep='      ')
print("outer after ids          ", id(list2), id(list2[0]), id(list2[0][0]), "\n", sep='     ')

list2 = [[1, 3], [5, 3], [7, 2]]
print("using listfunction2(list2)")
print("outer before elements   ", list2, list2[0], list2[0][0], sep='      ')
print("outer before ids         ", id(list2), id(list2[0]), id(list2[0][0]), sep='     ')
listfunction2(list2)         # uses a mutable list object, everything's changeable, adresses are the same
print("outer after elements    ", list2, list2[0], list2[0][0], sep='      ')
print("outer after ids          ", id(list2), id(list2[0]), id(list2[0][0]), "\n", sep='     ')


list2 = [[1, 3], [5, 3], [7, 2]]
print("using listfunction2(list2.copy())")
print("outer before elements   ", list2, list2[0], list2[0][0], sep='      ')
print("outer before ids         ", id(list2), id(list2[0]), id(list2[0][0]), sep='     ')
listfunction2(list2.copy())         # płytkie kopiowanie
# original is mutable
print("outer after elements    ", list2, list2[0], list2[0][0], sep='      ')
print("outer after ids          ", id(list2), id(list2[0]), id(list2[0][0]), "\n", sep='     ')


list2 = [[1, 3], [5, 3], [7, 2]]
print("using listfunction2(copy.deepcopy(list2))")
print("outer before elements   ", list2, list2[0], list2[0][0], sep='      ')
print("outer before ids         ", id(list2), id(list2[0]), id(list2[0][0]), sep='     ')
listfunction2(copy.deepcopy(list2))     # głębokie kopiowanie
# original is immutable
print("outer after elements    ", list2, list2[0], list2[0][0], sep='      ')
print("outer after ids          ", id(list2), id(list2[0]), id(list2[0][0]), sep='     ')
