import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
# response = requests.get("https://google.pl")


def count_task_frequency(tasks):
    completedTasksFrequencyByUser = dict()
    for entry in tasks:
        if entry["completed"]:
            try:
                completedTasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTasksFrequencyByUser[entry["userId"]] = 1
    return completedTasksFrequencyByUser


def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]


def users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTasksFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTasksFrequencyByUser.items():
        if numberOfCompletedTask == maxAmountOfCompletedTask:
            usersIdWithMaxCompletedAmountOfTasks.append(userId)
    return usersIdWithMaxCompletedAmountOfTasks


try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    completedTasksFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = users_with_top_completed_tasks(completedTasksFrequencyByUser)
