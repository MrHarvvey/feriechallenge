"""Napisz program, który importuje katalog z dowolnej biblioteki (np. API Biblioteki Narodowej http://data.bn.org.pl/ - przykład użycia: http://data.bn.org.pl/api/bibs.json?author=Andrzej+Sapkowski&amp;kind=ksi%C4%85%C5%BCka). Użytkownik może podać autora i program pokaże mu, jakie książki tego autora są w zbiorach biblioteki. Następnie daj użytkownikowi możliwość “wypożyczania” i “zwracania” książek - posiadane pozycje są składowane w pliku zawierającym pewien identyfikujący zbiór danych, np. tytuł, autor, wydawnictwo, rok wydania (możesz też użyć lokalnej bazy danych), w przypadku “wypożyczenia” książki są do niego dodawane, a w przypadku “zwracania” usuwane.


Propozycja rozszerzenia: W prostym przypadku lokalne “wypożyczanie” nie ma wpływu na katalog biblioteki, czyli w teorii można wypożyczyć książkę nieskończoną liczbę razy. Zabezpiecz program w taki sposób, aby podczas pobierania danych rozpoznawał też pozycje “wypożyczone” lokalnie i nie pokazywał ich już jako wyniki wyszukiwania."""

import requests

def get_books(author):
    url = "http://data.bn.org.pl/api/bibs.json?author=" + author
    response = requests.request("GET", url)
    return response.json(), print(response.text)

class Book:
    #constructor
    def __init__(self, id, title, author, publisher):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.is_borowed = False

    def __str__(self):
        return f"Title: {self.title}\nAuthor:{self.author}\nPublisher:{self.publisher}\n\n"

    # Function to create and append new student
    def add_new_book(self, id, title, author, publisher):
        ob = Book(id, title, author, publisher)
        ls.append(ob)

    # Function to display book details
    def display(self, ob):
         print("Id   : ", ob.id)
         print("title : ", ob.title)
         print("author : ", ob.author)
         print("publisher : ", ob.publisher)
         print("\n")

    def is_borowed(self):
        return self.is_borowed

    def search(self, id):
        for i in range(ls.__len__()):
            if(ls[i].id == id):
                return i


# Create a list to add Books
ls =[]

obj = Book("123", "OSkar", "jazebina", "publikacja")
obj.add_new_book("12325", "OSkar21", "jazebina12", "publikacja1231")
obj.add_new_book("12326", "OSkar21", "jazebina12", "publikacja1231")


book = Book.search(obj, "123")
print(book)
#
# def list_of_books(json_parse):
#     for where in json_parse['bibs']:
#         print(where)
#         Book.add_new_book(where['id'], where['title'], where['author'], where['publisher'])
#
#
# list_of_books(get_books("Sienkiewicz"))
#
# print(ls)

# for book in dic_books:
#     print(dic_books[book].is_borowed)
