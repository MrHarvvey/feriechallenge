import requests
import os

clear = lambda: os.system('clear')


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
        return f"ID: {self.ids}\n Title: {self.title}\nAuthor:{self.author}\nPublisher:{self.publisher}\nis borowed: {is_borowed}"

    # Function to create and append new book
    def add_new_book(self, ids, title, author, publisher):
        is_borowed = False
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

    # Function to lend book

    def lend_book(self, ids):
        for i in range(ls.__len__()):
            if(ls[i].ids == ids):
                ls[i].is_borowed = True
                print("book is borowed")
    # Function to lend book
    def return_book(self, ids):
        for i in range(ls.__len__()):
            if(ls[i].ids == ids):
                ls[i].is_borowed = False
                print("book is returned")

    def search(self, ids):
        for i in range(ls.__len__()):
            if(ls[i].ids == ids):
                return ls[i]



def get_books(author):
    url = "http://data.bn.org.pl/api/bibs.json?author=" + author
    response = requests.request("GET", url)
    return response.json()


def list_of_books(json_parse):
    for idx, where in enumerate(json_parse['bibs']):
        print(f"book {idx} added")
        obj.add_new_book(str(where['id']), where['title'], where['author'], where['publisher'])
# Create a list to add Books



ls =[]

obj = Book(" ", "0", "0", "0")





while True:
    print("\n1.Add new Book\n2.Display Book Details\n3.Lend a book \n4.Return Book\n5.Display all Books\n6.Import Books from library\n7.Exit")
    try:
        what_to_do = int(input("Enter choice:"))
    except ValueError:
        print("Sorry, i dont understand use only numbers")
        continue
    if what_to_do == 1:
        ids = input("Enter ids of the book: ")
        title = input("Enter title of the book: ")
        author = input("Enter author of the book: ")
        publisher = input("Enter publisher of the book: ")
        clear()
        if obj.search(ids) == None:
            obj.add_new_book(ids, title, author, publisher)
            print("book added")
        else:
            print("Book with this id exist")
    elif what_to_do == 2:
        ids = input("Enter the book you are looking for: ")
        clear()
        if obj.search(ids) == None:
            print("book not find")
        else:
            print(obj.search(ids))
    elif what_to_do == 3:
        ids = input("Enter id of the book you want to lend: ")
        clear()
        if obj.search(ids) == None:
            ids = input("Book not found Try Again: ")
            clear()
        else:
            obj.lend_book(ids)
    elif what_to_do == 4:
        ids = input("Enter id of the book you want to return: ")
        clear()
        if obj.search(ids) == None:
            ids = input("Book not found Try Again: ")
            clear()
        else:
            obj.return_book(ids)
    elif what_to_do == 5:
        clear()
        for i in range(ls.__len__()):
            print(f'{ls[i]}\n\n')
    elif what_to_do == 6:
        author = input("Enter author to import books: ")
        list_of_books(get_books(author))
    else:
        print("Thank You !")
        break


