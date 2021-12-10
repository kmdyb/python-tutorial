import requests
import json
import webbrowser
import credentials


def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format", response.text)
    else:
        return content


def get_favourite_cats(userId):
    params = {
        "sub_id": userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params, headers=credentials.headers)

    return get_json_content_from_response(r)


def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search/', headers=credentials.headers)
    return get_json_content_from_response(r)


def add_favourite_cat(catId, userId):
    catData = {
        "image_id": catId,
        "sub_id": userId
    }
    r = requests.post('https://api.thecatapi.com/v1/favourites/', json=catData, headers=credentials.headers)

    return get_json_content_from_response(r)


def remove_favourite_cat(userId, favouriteCatToRemove):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/'+favouriteCatToRemove, headers=credentials.headers)

    return get_json_content_from_response(r)


def picture_in_browser(link):
    browser_answer = input("Czy chcesz otworzyć zdjęcie w przeglądarce? T/N ")
    if browser_answer.upper() == "T":
        webbrowser.open_new_tab(link)
    else:
        print("Ok, idziemy dalej.")


userId = "agh2m"
favouriteCats = get_favourite_cats(userId)
print("Zalogowano jako ", userId, ". Twoje ulubione koty to:", sep='')
for favCat in favouriteCats:
    print(favCat["id"], favCat["image"]["url"])

removeFavouriteCat = input("\nCzy chcesz usunąć kota z ulubionych? T/N ")
if removeFavouriteCat.upper() == "T":
    favouriteCatToRemove = input("Który to będzie kot? Podaj jego id: ")
    remove_favourite_cat(userId, favouriteCatToRemove)
    print("Kotek posmutniał.")
else:
    print("Kotki się cieszą.")

randCat = input("\nCzy chcesz wylosować kota? T/N ")
if randCat.upper() == "T":
    randomCat = get_random_cat()
    print("Wylosowano kota:", randomCat[0]["url"])
    picture_in_browser(randomCat[0]["url"])

    addToFavourites = input("\nCzy chcesz dodać go do ulubionych? T/N ")
    if addToFavourites.upper() == "T":
        add_favourite_cat(randomCat[0]["id"], userId)
        print("Kotek się cieszy.")
    else:
        print("Kotek posmutniał.")

else:
    print("Ok, kończę program.")
