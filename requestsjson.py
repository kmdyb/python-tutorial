import requests
import json


def count_completed_tasks(alltasks):
    completedtasksinner = dict()
    for entry in alltasks:
        if entry["completed"]:
            try:
                completedtasksinner[entry["userId"]] += 1
            except KeyError:
                completedtasksinner[entry["userId"]] = 1
    return completedtasksinner


def users_with_top_completed_tasks(completedtasksinner):
    topusersinner = []
    maxcompletedtasks = max(completedtasksinner.values())
    for userId, numberOfCompletedTask in completedtasksinner.items():
        if numberOfCompletedTask == maxcompletedtasks:
            topusersinner.append(userId)
    return topusersinner


"""def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]"""


response = requests.get("https://jsonplaceholder.typicode.com/todos")
try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    completedtasks = count_completed_tasks(tasks)
    topusers = users_with_top_completed_tasks(completedtasks)

"""
# sposób 1
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
for user in users:
    if user["id"] in topusers:
        print(user["name"])
        topusers.remove(user["id"])
"""
"""
# sposób 2
print(topusers)
for userID in topusers:
    # response = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userID))
    response = requests.get("https://jsonplaceholder.typicode.com/users/", params="id="+str(userID))
    user = response.json()
    print(user)
    print(userID)
"""
# sposób 3


def change_list_into_conj_of_param(my_list, key="id"):
    f_conj_param = key + "="
    last = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if i == last:
            f_conj_param += str(item)
        else:
            f_conj_param += str(item) + "&" + key + "="
    return f_conj_param


conj_param = change_list_into_conj_of_param(topusers)
response = requests.get("https://jsonplaceholder.typicode.com/users/", params=conj_param)
users = response.json()
for user in users:
    print(user["name"])
