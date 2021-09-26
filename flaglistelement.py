# program porównuyjący element listy z oczekiwaną wartością

a_list = ["expected value", "other value"]
flag = False

if len(a_list) > 0 and a_list[0] == "expected value":
    flag = True

print(flag)
