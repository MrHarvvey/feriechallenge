"""Napisz program, który importuje katalog z dowolnej biblioteki (np. API Biblioteki Narodowej http://data.bn.org.pl/ - przykład użycia: http://data.bn.org.pl/api/bibs.json?author=Andrzej+Sapkowski&amp;kind=ksi%C4%85%C5%BCka). Użytkownik może podać autora i program pokaże mu, jakie książki tego autora są w zbiorach biblioteki. Następnie daj użytkownikowi możliwość “wypożyczania” i “zwracania” książek - posiadane pozycje są składowane w pliku zawierającym pewien identyfikujący zbiór danych, np. tytuł, autor, wydawnictwo, rok wydania (możesz też użyć lokalnej bazy danych), w przypadku “wypożyczenia” książki są do niego dodawane, a w przypadku “zwracania” usuwane.


Propozycja rozszerzenia: W prostym przypadku lokalne “wypożyczanie” nie ma wpływu na katalog biblioteki, czyli w teorii można wypożyczyć książkę nieskończoną liczbę razy. Zabezpiecz program w taki sposób, aby podczas pobierania danych rozpoznawał też pozycje “wypożyczone” lokalnie i nie pokazywał ich już jako wyniki wyszukiwania."""

import requests

def get_books(author):
    url = "http://data.bn.org.pl/api/bibs.json?author=" + author
    response = requests.request("GET", url)
    return response.json()


class Book:
    def __init__(self, id, title, author, publisher):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.is_borowed = False
    def __str__(self):
        return f"Title: {self.title}\nAuthor:{self.author}\nPublisher:{self.publisher}\n\n"

    def is_borowed(self):
        return self.is_borowed


dic_books = {}

def list_of_books(json_parse):
    for ix, where in enumerate(json_parse['bibs']):
        dic_books[f"book_{ix}"] = Book(where['id'], where['title'], where['author'], where['publisher'])


list_of_books(get_books("Sienkiewicz"))

for book in dic_books:
    print(dic_books[book].is_borowed)
