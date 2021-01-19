"""Napisz program, który importuje katalog z dowolnej biblioteki (np. API Biblioteki Narodowej http://data.bn.org.pl/ - przykład użycia: http://data.bn.org.pl/api/bibs.json?author=Andrzej+Sapkowski&amp;kind=ksi%C4%85%C5%BCka). Użytkownik może podać autora i program pokaże mu, jakie książki tego autora są w zbiorach biblioteki. Następnie daj użytkownikowi możliwość “wypożyczania” i “zwracania” książek - posiadane pozycje są składowane w pliku zawierającym pewien identyfikujący zbiór danych, np. tytuł, autor, wydawnictwo, rok wydania (możesz też użyć lokalnej bazy danych), w przypadku “wypożyczenia” książki są do niego dodawane, a w przypadku “zwracania” usuwane.


Propozycja rozszerzenia: W prostym przypadku lokalne “wypożyczanie” nie ma wpływu na katalog biblioteki, czyli w teorii można wypożyczyć książkę nieskończoną liczbę razy. Zabezpiecz program w taki sposób, aby podczas pobierania danych rozpoznawał też pozycje “wypożyczone” lokalnie i nie pokazywał ich już jako wyniki wyszukiwania."""

import requests


class Book:
    #constructor
    def __init__(self, ids, title, author, publisher):
        self.ids = ids
        self.title = title
        self.author = author
        self.publisher = publisher
        self.is_borowed = False

    def __str__(self):
        if self.is_borowed == False:
            is_borowed = "no"
        else:
            is_borowed = "yes"
        return f"Title: {self.title}\nAuthor:{self.author}\nPublisher:{self.publisher}\nis borowed: {is_borowed}"

    # Function to create and append new student
    def add_new_book(self, ids, title, author, publisher):
        ob = Book(ids, title, author, publisher)
        ls.append(ob)

    # Function to display book details
    def display(self, ob):
        print("Id   : ", ob.ids)
        print("title : ", ob.title)
        print("author : ", ob.author)
        print("publisher : ", ob.publisher)
        if ob.is_borowed == False:
            is_borowed = "no"
            print("Is borowed : ", is_borowed)
        else:
            is_borowed = "yes"
            print("Is borowed : ", is_borowed)


    def lend_book(self, ids):
        for i in range(ls.__len__()):
            if(ls[i].ids == ids):
                self.is_borowed = True
                print("book is borowed")

    def return_book(self, ids):
        for i in range(ls.__len__()):
            if(ls[i].ids == ids):
                self.is_borowed = True
                print("book is returned")

    def search(self, ids):
        for i in range(ls.__len__()):
            if(ls[i].ids == ids):
                return ls[i]



def get_books(author):
    url = "http://data.bn.org.pl/api/bibs.json?author=" + author
    response = requests.request("GET", url)
    return response.json(), print(response.text)


# Create a list to add Books
ls =[]

obj = Book(" ", "0", "0", "0")
print("\n1.Add new Book\n2.Display Book Details\n3.Lend a book \n4.Return Book\n5.Exit")

while True:
    what_to_do = int(input("Enter choice:"))
    if what_to_do == 1:
        ids = input("Enter ids of the book")
        title = input("Enter title of the book")
        author = input("Enter author of the book")
        publisher = input("Enter publisher of the book")
        obj.add_new_book(ids, title, author, publisher)
    elif what_to_do == 2:
        ids = input("Enter the book you are looking for")
        if obj.search(ids) == None:
            print("book not find")
        else:
            print(obj.search(ids))
    elif what_to_do == 3:
        ids = input("Enter id of the book you want to lend")
        if obj.search(ids) == None:
            ids = input("Book not found Try Again: ")
        else:
            obj.lend_book(ids)
            print(obj.search(ids))
    else:
        print("Thank You !")
        break


#book = Book.search(obj, "12325")
#print(book)
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
