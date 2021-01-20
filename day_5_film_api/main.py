"""#MOVIE #FINDER
Przy wykorzystaniu API (np. IMDB) wyszukaj wszystkie części filmu zadanego w wyszukiwaniu (np. Rambo, Scary Movie, Shrek). Można przyjąć założenie, że wszystkie filmy “z serii” muszą zawierać szukany ciąg - czasem zdarzają się błędne wyniki wyszukiwania z baz, można je spróbować odfiltrować. Wyświetl dla każdego podstawowe informacje np. rok, długość, ocena, spis aktorów (pierwszych 5 z listy).
Przykładowe API do wykorzystania:
https://rapidapi.com/apidojo/api/imdb8/endpoints - do wyszukania filmów z daną nazwą (do odfiltrowania można użyć warunku, że dany rekord posiada nazwę i rok wydania)
https://rapidapi.com/.../imdb-internet-movie-database... - pobranie szczegółów o danym filmie"""


import requests
import json

def related_film(film):
    querystring = {"q": film}
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    headers = {
        'x-rapidapi-key': "bf66404f35mshecd7b9b3525744bp1d79a8jsna94048c27ef6",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


def parsing_values(text_json):
    parsed_json = json.loads(text_json)
    for i in range(0, 5):
        try:
            title = parsed_json["d"][i]["l"]
            year = parsed_json["d"][i]["y"]
            actores = parsed_json["d"][i]["s"]
            rank =parsed_json["d"][i]["rank"]
            print(f"{title} \n {year} year, {actores},  {rank} in rank")
        except Exception as e:
            print(f"no title find {e}")


parsing_values(related_film(input("please enter the movie for which you want to find relations: ")))



