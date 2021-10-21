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


"""def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]"""


def users_with_top_completed_tasks(completedtasksinner):
    topusersinner = []
    maxcompletedtasks = max(completedtasksinner.values())
    for userId, numberOfCompletedTask in completedtasksinner.items():
        if numberOfCompletedTask == maxcompletedtasks:
            topusersinner.append(userId)
    return topusersinner


response = requests.get("https://jsonplaceholder.typicode.com/todos")
try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    completedtasks = count_completed_tasks(tasks)
    topusers = users_with_top_completed_tasks(completedtasks)
