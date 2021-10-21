import requests


siteaddress = "http://www.google.com"
response = requests.get(siteaddress)
print(response)
print(response.status_code)

with open("siterequest.txt", "w", encoding="UTF-8") as file:
    file.write(siteaddress)
    file.write(response.text)

# filtrowanie stron ---- kod działa tylko przy poprawnych stronach... do poprawy
strony = [siteaddress, "http://www.google.pl", "http://www.pap.pl", "http://www.pap.gov.pl"]
stronyok = []
for element in strony:
    try:
        if requests.get(element).status_code == 200:
            stronyok.append(element)
    except requests.RequestException:
        continue
print("strony:", strony)
print("działające:", stronyok)
