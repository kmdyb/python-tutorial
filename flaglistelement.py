# program porównuyjący element listy z oczekiwaną wartością

a_list = ["expected value", "other value"]
flag = False

if len(a_list) > 0 and a_list[0] == "expected value":
    flag = True

# another way of doing it
# flag = len(a_list) > 0 and a_list[0] == "expected value"

print(flag)
