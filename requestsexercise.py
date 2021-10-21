import requests


siteaddress = "http://www.google.com"
response = requests.get(siteaddress)
print(response)
print(response.status_code)

with open("siterequest.txt", "w", encoding="UTF-8") as file:
    file.write(siteaddress)
    file.write(response.text)
