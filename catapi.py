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


def get_favourite_cats(user_id):
    params = {
        "sub_id": user_id
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params, headers=credentials.headers)

    return get_json_content_from_response(r)


def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search/', headers=credentials.headers)
    return get_json_content_from_response(r)


def add_favourite_cat(cat_id, user_id):
    cat_data = {
        "image_id": cat_id,
        "sub_id": user_id
    }
    r = requests.post('https://api.thecatapi.com/v1/favourites/', json=cat_data, headers=credentials.headers)

    return get_json_content_from_response(r)


def remove_favourite_cat(cat_to_remove):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/'+cat_to_remove, headers=credentials.headers)

    return get_json_content_from_response(r)


def picture_in_browser(link):
    browser_answer = input("Czy chcesz otworzyć zdjęcie w przeglądarce? T/N ")
    if browser_answer.upper() == "T":
        webbrowser.open_new_tab(link)
    else:
        print("Ok, idziemy dalej.")


userId = "Kiwi"
favouriteCats = get_favourite_cats(userId)
print("Zalogowano jako ", userId, ". Twoje ulubione koty to:", sep='')
for favCat in favouriteCats:
    print(favCat["id"], favCat["image"]["url"])

cats = {
    cat["id"]: cat["image"]["url"]
    for cat in favouriteCats
}

see_cat = input("Czy chcesz zobaczyć któregoś z nich? T/N ")
if see_cat.upper() == "T":
    see_cat_id = int(input("Podaj jego id: "))
    link = cats[see_cat_id]
    picture_in_browser(link)

else:
    print("Ok, idziemy dalej.")

removeFavouriteCat = input("\nCzy chcesz któregoś kota usunąć z ulubionych? T/N ")
if removeFavouriteCat.upper() == "T":
    favourite_cat_to_remove = input("Który to będzie kot? Podaj jego id: ")
    remove_favourite_cat(favourite_cat_to_remove)
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
