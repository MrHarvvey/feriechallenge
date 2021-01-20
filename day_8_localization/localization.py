"""Napisz program liczący odległość liniową między dwoma dowolnymi punktami na mapie, wykorzystujący ich współrzędne geograficzne (długość i szerokość geograficzną). Wykorzystaj dowolny algorytm, np. https://pl.wikibooks.org/.../Astrono.../Odleg%C5%82o%C5%9Bci
Skorzystaj z API (np. https://rapidapi.com/trueway/api/trueway-geocoding), żeby obliczyć odległość pomiędzy twoim adresem, a charakterystycznymi punktami np. Wieżą Eiffla czy Tadź Mahal.
Propozycja rozszerzenia: zamiast podawać swój adres, użyj geolokalizacji 🙂"""


import haversine as hs
import requests
import json

import geocoder

print(" This is your program to checking distance between two citys, if you want check distance beetwen your computer localization and other city in first city write 'me'")


def get_localization_info(localization):
    try:
        url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
        querystring = {"address": localization, "language":"en"}
        headers = {
            'x-rapidapi-key': "bf66404f35mshecd7b9b3525744bp1d79a8jsna94048c27ef6",
            'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
    except Exception as e:
        raise print(e)
    return response.text


def localiation_x_y(data_json):
    #input string parse data and return location lat and lng
    try:
        json_parse = json.loads(data_json)
        localion_lat = json_parse['results'][0]['location']['lat']
        localion_lng = json_parse['results'][0]['location']['lng']
    except Exception as e:
        raise print(e)
    return localion_lat, localion_lng

def get_distance(loc1, loc2):
    #returning distance in kilomiters
    return str(int(hs.haversine(loc1, loc2))) + "km"


def distance_me():
    loc1 = input("first city: ")
    if loc1.lower() == "me":
        my_localization = geocoder.ip('me')
        loc1 = my_localization.latlng
        loc2 = localiation_x_y(get_localization_info(input("second city: ")))
        distance = get_distance(loc1, loc2)
        print(distance)
    else:
        loc1 = localiation_x_y(get_localization_info(loc1))
        loc2 = localiation_x_y(get_localization_info(input("second city: ")))
        distance = get_distance(loc1, loc2)
        print(distance)


distance_me()


# Press the green button in the gutter to run the script.
