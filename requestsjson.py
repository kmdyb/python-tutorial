import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/users")
# response = requests.get("https://google.pl")
try:
    users = response.json()     # metoda .json() sprawdza czy ma do czynienia z formatem json
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    print("Wszystko OK")
