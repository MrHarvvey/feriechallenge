🎄️# 10 day coding challenge with Python
This repository contains 10 day winter-break coding challenge. Each day there was a problem to solve. The idea of the challenge is to learn something new and adapt the problem to own programming skills. 

Event link: https://www.facebook.com/events/843253696243420?active_tab=about

What I learned during the challenge?

• Discovered a wide range of Python modules,

• Got familliar with many different APIs, processing requests and using the data in the code,

• Improved my knowledge of modules previously known to me,

• Coding regularily, the challenge gave me a routine to follow and problems to solve, which I often extended to make more challenging. 

• Became more fluent with reading documentation.

 👨‍💻️most challenging was build own library in challange 9, cost more time than other projects, i had to thing how import correctly books/lend and return them. I had ocassion to make classes which i try improve right now  
 

 ☎️day_1_anagram 
 
 No to startujemy z wyzwaniem! 🏁 Na pierwszy dzień coś prostego, żeby się dobrze rozgrzać i nie zniechęcić 🙂
#PALINDROMY I #ANAGRAMY
Napisz program, który prosi użytkownika o podanie dowolnego napisu. Następnie program wyświetla na ekranie to słowo wspak (od prawej do lewej) i wyświetla komunikat czy to wyrażenie jest palindromem (czyli czytane wspak daje do samo wyrażenie np. “ala”, “Kobyła ma mały bok” (inne przykłady: http://www.palindromy.pl/pal_kr.php). Podczas sprawdzania ignoruj wielkość liter oraz znaki niebędące literami. Następnie wywołaj dowolną stronę internetową, która pokaże anagramy oraz słowa utworzone po usunięciu liter, np. https://poocoo.pl/scrabble-slowa-z-liter/hardcoder 
Propozycja rozszerzenia: samodzielnie wyszukaj anagramy i słowa utworzone po usunięciu liter z podanego słowa, na przykład wykorzystując słownik wspomniany na stronie https://anagramy.wybornie.com/ 
Kody / pytania / wątpliwości / wszystkie inne miłe rzeczy można wrzucać w komentarzach! 🙂

☘️day_2_wheather

"""Wczoraj poradziliście sobie świetnie! 🙂 No to dzisiaj trochę podkręcamy poziom, żeby nie było nudno 😎 (ale drodzy początkujący, spokojnie! poziomy będą oscylować, a nie tylko iść do góry!) 🦸‍♀️🦸‍♂️
Dzisiaj proponujemy pokorzystać trochę z API i zaciągnąć trochę danych "na żywo" (proponowane przez nas rapidapi ma tą zaletę, że jest darmowe po założeniu konta oraz można od razu pobrać snippety kodu w danym języku - ale można korzystać oczywiście z dowolnego źródła i techniki, web scrapping też dozwolony!). Jeśli ktoś ma dużo czasu zawsze można też do tej bajki dołozyć wizualizację 🤩
#KARTKA #Z #KALENDARZA
Napisz program, który po uruchomieniu wyświetla w czytelnej formie aktualną datę, godzinę, dzień tygodnia i pogodę/temperaturę/ciśnienie w zadanym mieście (wykorzystaj np. https://rapidapi.com/commu.../api/open-weather-map/endpoints - pamiętaj o poprawnym przeliczeniu jednostek np. temperatura z kelwinów na stopnie) oraz losowy cytat (np. https://type.fit/api/quotes ). Wykorzystaj requests i datetime.
Propozycja rozszerzenia: Wyświetl również bieżący czas dla miast w różnych strefach czasowych (np. Pekin, Sydney, Waszyngton, Londyn) - wykorzystaj np. pytz: https://pypi.org/project/pytz/ oraz wyświetl listę osób obchodzących imieniny (poszukaj otwartej bazy danych lub wykorzystaj prosty web scrapping np. z wykorzystaniem: https://imienniczek.pl/widget/js )."""

🔎️day_3_email_send
"#feriechallenge #program3
"#No to trzeci dzień wyzwania! 🤩 Dzisiaj zapewne większość ma wolne (a zresztą i tak nie ma gdzie wyjść...), więc proponujemy coś nieco bardziej skomplikowanego i chyba najbardziej #praktycznego - sami niedawno potrzebowaliśmy takiej funkcjonalności w naszej firmie do upraszczania życia 💌 Przenieśmy się do świata początkującego korpo lub nowoczesnego "zdigitalizowanego" urzędu 🏤, w którym systemy nie są skonfigurowane, o bazach danych nikt nie słyszał, więc są przechowywane w tabelkach w Excelu... 📝
#MAIL #SENDER
"#Stwórz prosty program, który będzie wysyłał spersonalizowany mailing do wybranych osób. “Bazą danych” jest plik Excela (aby było “ciekawiej” 😉 ) lub CSV, zawierający dwie kolumny z nagłówkami: “E-mail” oraz “Imię i nazwisko” (zakładamy, że zawsze w takiej kolejności, a imię i nazwisko są oddzielone spacją). Do użytkowników należy wysłać maila z tematem “Your image” oraz spersonalizowaną prostą treścią np. “Hi {Imię}! it’s file generated for you”. Dodatkowo w załączniku maila znajduje się plik graficzny o nazwie “{Imię}_{Nazwisko}_image.png” (pliki są w zadanej lokalizacji). Odpowiednio zabezpiecz program (np. brakujący plik Excela, brakujące dane w Excelu, brak pliku png) oraz zabezpiecz przed spamowaniem (np. jeden mail wysyłany co 1 sekundę). Mogą przydać się moduły: smtplib, email, ssl, xlrd, re, os.
"#Propozycje rozszerzenia: dodaj opcję wysyłania maili z treścią w HTML oraz walidator poprawności maila (np. używając wyrażeń regularnych - moduł re)."

🥜️day_4_fit_app

"""##feriechallenge #program4
Hej, witamy w drugi poniedziałek w tym tygodniu, na szczęście jutro też drugi piątek 😎 Dzisiaj zgodnie z obietnicą program, który jest w stanie zrobić każdy początkujący i da się go zrobić bez skomplikowanych zewnętrznych modułów 🙂 Program nawiązuje do tego, że ostatnio co chwilę są jakieś święta, a wiadomo czemu to sprzyja, zwłaszcza w kombinacji z zamknięciem w domach i zamknięciem obiektów sportowych 😋🥓🍽️ Treść można dość luźno interpretować, ważne, żeby sens był zachowany - obliczanie BMI i uzależnienie od niego w jakiś sposób planu treningowego 🚴
#FAT #BURNER
Napisz program, który na podstawie masy [kg] i wzrostu [cm] wylicza wskaźnik BMI (https://en.wikipedia.org/wiki/Body_mass_index) oraz informuje użytkownika, w jakim jest zakresie. Zakresy można wpisać “z palca” (ale może nieco mądrzej niż ciągiem if-elif-else dla każdego zakresu! 😉 ) albo odczytać z dowolnego API, np. https://rapidapi.com/navii/api/bmi-calculator . Następnie program losuje jedną z aktywności fizycznych oraz czas jej wykonania, np. bieganie przez 30 minut. Czas nie może być dłuższy niż podany przez użytkownika (maksymalny czas, który można poświęcić na ćwiczenia). Zadbaj o to, aby czas aktywności był jakoś uzależniony od BMI (na przykład osoba z niedowagą nie powinna ćwiczyć mniej niż osoba o wadze normalnej - ustal pewien minimalny czas; ale już osoba z nadwagą powinna ćwiczyć dłużej - ustal odpowiedni nieliniowy mnożnik, tak aby nie przekroczyć maksimum). Utwórz w ten sposób plan treningowy na 7 następnych dni, wyniki zapisując do pliku .txt.
Propozycja rozszerzenia: przygotuj urozmaicony plan treningowy uwzględniający maksymalny czas wpisany przez użytkownika - kilka aktywności fizycznych ma wypełniać całą dzienną ilość czasu, mają zajmować jakąs ustaloną minimalną długość (np. 10 minut) oraz nie mogą się powtarzać jednego dnia.
"""
🎨️day_5_film_api

"""#MOVIE #FINDER
Przy wykorzystaniu API (np. IMDB) wyszukaj wszystkie części filmu zadanego w wyszukiwaniu (np. Rambo, Scary Movie, Shrek). Można przyjąć założenie, że wszystkie filmy “z serii” muszą zawierać szukany ciąg - czasem zdarzają się błędne wyniki wyszukiwania z baz, można je spróbować odfiltrować. Wyświetl dla każdego podstawowe informacje np. rok, długość, ocena, spis aktorów (pierwszych 5 z listy).
Przykładowe API do wykorzystania:
https://rapidapi.com/apidojo/api/imdb8/endpoints - do wyszukania filmów z daną nazwą (do odfiltrowania można użyć warunku, że dany rekord posiada nazwę i rok wydania)
https://rapidapi.com/.../imdb-internet-movie-database... - pobranie szczegółów o danym filmie"""

🏘️day_6_resizer

"""Napisz program, który w wybranej lokalizacji odczyta wszystkie pliki graficzne (w określonych formatach, np. jpg, png, bmp itp.), następnie zmniejszy ich rozdzielczość o 50% i zapisze je w podkatalogu “smaller” z odpowiednimi nazwami. Wykorzystaj pillow lub inną bibliotekę do pracy z obrazami.


Propozycja rozszerzenia: Oblicz ile miejsca na dysku można oszczędzić po kompresji (odczytaj rozmiar plików w pierwotnym folderze oraz "smaller" i porównaj obie wartości - bezwzględnie i w %)"""

🎁️day_7_password

"""Napisz program do generowania losowych haseł o zadanej przez użytkownika długości. Hasło musi spełniać zadane warunki np. co najmniej jedna liczba, co najmniej po jednej dużej i małej literze. Warto skorzystać z modułów string i secrets.
Propozycja rozszerzenia: Po wygenerowaniu hasła skopiuj je do schowka systemowego 🙂"""

🚅️day_8_localization

"""Napisz program liczący odległość liniową między dwoma dowolnymi punktami na mapie, wykorzystujący ich współrzędne geograficzne (długość i szerokość geograficzną). Wykorzystaj dowolny algorytm, np. https://pl.wikibooks.org/.../Astrono.../Odleg%C5%82o%C5%9Bci
Skorzystaj z API (np. https://rapidapi.com/trueway/api/trueway-geocoding), żeby obliczyć odległość pomiędzy twoim adresem, a charakterystycznymi punktami np. Wieżą Eiffla czy Tadź Mahal.
Propozycja rozszerzenia: zamiast podawać swój adres, użyj geolokalizacji 🙂"""

🎸️day_9_home_library

"""Napisz program, który importuje katalog z dowolnej biblioteki (np. API Biblioteki Narodowej http://data.bn.org.pl/ - przykład użycia: http://data.bn.org.pl/api/bibs.json?author=Andrzej+Sapkowski&amp;kind=ksi%C4%85%C5%BCka). Użytkownik może podać autora i program pokaże mu, jakie książki tego autora są w zbiorach biblioteki. Następnie daj użytkownikowi możliwość “wypożyczania” i “zwracania” książek - posiadane pozycje są składowane w pliku zawierającym pewien identyfikujący zbiór danych, np. tytuł, autor, wydawnictwo, rok wydania (możesz też użyć lokalnej bazy danych), w przypadku “wypożyczenia” książki są do niego dodawane, a w przypadku “zwracania” usuwane.


Propozycja rozszerzenia: W prostym przypadku lokalne “wypożyczanie” nie ma wpływu na katalog biblioteki, czyli w teorii można wypożyczyć książkę nieskończoną liczbę razy. Zabezpiecz program w taki sposób, aby podczas pobierania danych rozpoznawał też pozycje “wypożyczone” lokalnie i nie pokazywał ich już jako wyniki wyszukiwania."""


🎫️day_10_summary
'''Napisz program, który odczytuje wszystkie pliki stworzone przez Ciebie podczas #feriechallenge - przeszukuje lokalne katalogi lub łączy się w tym celu z Githubem. Postaraj się jak najmniej hardcodować i na przykład nie podawaj listy wszystkich plików ręcznie 🙂  Następnie wykorzystując swój sposób katalogowania programów automat odczytuje i wyświetla takie informacje:
-> do ilu zadań z 10 napisało się kod
-> liczba linijek kodu napisanych w każdym zadaniu (bez uwzględniania pustych!) oraz sumaryczna liczba linijek
-> liczba unikalnych słów użytych we wszystkich programach oraz najczęściej występujące słowo
-> lista i liczba słów kluczowych użyta podczas całego challenge (wykorzystaj moduł keywords)
-> lista i liczba zaimportowanych modułów we wszystkich programach
Propozycja rozszerzenia: Po prostu miej odwagę i pochwal się outputem swojego programu! - opublikuj posta z tagiem #feriechallenge i zostaw lajka na naszej stronie, będzie nam miło 🙂 Możesz też oczywiście umieścić jakieś dodatkowe statystyki.'''


