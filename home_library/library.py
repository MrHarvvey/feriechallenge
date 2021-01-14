"""Napisz program, który importuje katalog z dowolnej biblioteki (np. API Biblioteki Narodowej http://data.bn.org.pl/ - przykład użycia: http://data.bn.org.pl/api/bibs.json?author=Andrzej+Sapkowski&amp;kind=ksi%C4%85%C5%BCka). Użytkownik może podać autora i program pokaże mu, jakie książki tego autora są w zbiorach biblioteki. Następnie daj użytkownikowi możliwość “wypożyczania” i “zwracania” książek - posiadane pozycje są składowane w pliku zawierającym pewien identyfikujący zbiór danych, np. tytuł, autor, wydawnictwo, rok wydania (możesz też użyć lokalnej bazy danych), w przypadku “wypożyczenia” książki są do niego dodawane, a w przypadku “zwracania” usuwane.


Propozycja rozszerzenia: W prostym przypadku lokalne “wypożyczanie” nie ma wpływu na katalog biblioteki, czyli w teorii można wypożyczyć książkę nieskończoną liczbę razy. Zabezpiecz program w taki sposób, aby podczas pobierania danych rozpoznawał też pozycje “wypożyczone” lokalnie i nie pokazywał ich już jako wyniki wyszukiwania."""

import requests





def get_books(author):
    url = "http://data.bn.org.pl/api/bibs.json?author=" + author
    response = requests.request("GET", url)
    return response.json()


get_books("Sienkiewicz")


def list_of_books(json_parse):
    for i in range(0, 9):
        print(json_parse['bibs'][i]['title'])
        print(json_parse['bibs'][i]['title'])
list_of_books(get_books("Sienkiewicz"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
