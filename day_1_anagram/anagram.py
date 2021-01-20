import re
import webbrowser
#palindrom

moj_string = input("Wpisz tekst: ")

#deleting special signs

def delete_specjal(data):
    return re.sub('[^A-Za-z]+', '', data)



if delete_specjal(moj_string).lower() == delete_specjal(moj_string[::-1].lower()):
    print(f"Twoj wyraz jest pantonimem: {moj_string[::-1]}")
    webbrowser.open('http://www.palindromy.pl')
else:
    print(f"Twoj wyraz nie jest pantonimem: {moj_string[::-1]}")

