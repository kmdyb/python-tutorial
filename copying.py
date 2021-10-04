def listfunction(somelist):
    print("infunc before        ", id(somelist), somelist)
    somelist.append(666)
    somelist[0] = 10
    print("infunc after         ", id(somelist), somelist)


def listfunction2(somelist):
    print("infunc before                    ", id(somelist), somelist)
    print("infunc before, list2[0]          ", id(list2[0]), list2[0])
    print("infunc before, list2[0][0]       ", id(list2[0][0]), list2[0][0])
    somelist.append(666)
    somelist[0][0] = 100
    print("infunc after                     ", id(somelist), somelist)
    print("infunc after, list2[0]           ", id(list2[0]), list2[0])
    print("infunc after, list2[0][0]        ", id(list2[0][0]), list2[0][0])


list1 = [1, 5, 7, 34]
list2 = [[1, 3], [5, 3], [7, 2]]

print("using listfunction(list1[:])")
print("outer before         ", id(list1), list1)
listfunction(list1[:])      # creates a copy to work on, event though a list is mutable
print("outer after          ", id(list1), list1, "\n")

print("using listfunction(list1)")
print("outer before         ", id(list1), list1)
listfunction(list1)         # uses a mutable list object
print("outer after          ", id(list1), list1, "\n")

print("using listfunction2(list2[:])")
print("outer before list2               ", id(list2), list2)
print("outer before list2[0]            ", id(list2[0]), list2[0])
print("outer before list2[0][0]         ", id(list2[0][0]), list2[0][0])
listfunction2(list2[:])      # creates a copy to work on, event though a list is mutable
print("outer after list2                ", id(list2), list2)
print("outer after list2[0]             ", id(list2[0]), list2[0])
print("outer after list2[0][0]          ", id(list2[0][0]), list2[0][0], "\n")

print("using listfunction2(list2)")
print("outer before, list2              ", id(list2), list2)
print("outer before, list2[0]           ", id(list2[0]), list2[0])
print("outer before, list2[0][0]        ", id(list2[0][0]), list2[0][0])
listfunction2(list2)         # uses a mutable list object
print("outer after, list2               ", id(list2), list2)
print("outer after, list2[0]            ", id(list2[0]), list2[0])
print("outer after, list2[0][0]         ", id(list2[0][0]), list2[0][0])
