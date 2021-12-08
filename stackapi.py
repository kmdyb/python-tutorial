import requests
import json
import pprint
import webbrowser

params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": "2021-12-01",
    "tagged": "python",
    "min": 7
}

r = requests.get("https://api.stackexchange.com/2.3/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        pprint.pprint(question["link"])
        webbrowser.open_new_tab(question["link"])
