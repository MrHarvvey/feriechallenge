"""##feriechallenge #program4
Hej, witamy w drugi poniedziałek w tym tygodniu, na szczęście jutro też drugi piątek 😎 Dzisiaj zgodnie z obietnicą program, który jest w stanie zrobić każdy początkujący i da się go zrobić bez skomplikowanych zewnętrznych modułów 🙂 Program nawiązuje do tego, że ostatnio co chwilę są jakieś święta, a wiadomo czemu to sprzyja, zwłaszcza w kombinacji z zamknięciem w domach i zamknięciem obiektów sportowych 😋🥓🍽️ Treść można dość luźno interpretować, ważne, żeby sens był zachowany - obliczanie BMI i uzależnienie od niego w jakiś sposób planu treningowego 🚴
#FAT #BURNER
Napisz program, który na podstawie masy [kg] i wzrostu [cm] wylicza wskaźnik BMI (https://en.wikipedia.org/wiki/Body_mass_index) oraz informuje użytkownika, w jakim jest zakresie. Zakresy można wpisać “z palca” (ale może nieco mądrzej niż ciągiem if-elif-else dla każdego zakresu! 😉 ) albo odczytać z dowolnego API, np. https://rapidapi.com/navii/api/bmi-calculator . Następnie program losuje jedną z aktywności fizycznych oraz czas jej wykonania, np. bieganie przez 30 minut. Czas nie może być dłuższy niż podany przez użytkownika (maksymalny czas, który można poświęcić na ćwiczenia). Zadbaj o to, aby czas aktywności był jakoś uzależniony od BMI (na przykład osoba z niedowagą nie powinna ćwiczyć mniej niż osoba o wadze normalnej - ustal pewien minimalny czas; ale już osoba z nadwagą powinna ćwiczyć dłużej - ustal odpowiedni nieliniowy mnożnik, tak aby nie przekroczyć maksimum). Utwórz w ten sposób plan treningowy na 7 następnych dni, wyniki zapisując do pliku .txt.
Propozycja rozszerzenia: przygotuj urozmaicony plan treningowy uwzględniający maksymalny czas wpisany przez użytkownika - kilka aktywności fizycznych ma wypełniać całą dzienną ilość czasu, mają zajmować jakąs ustaloną minimalną długość (np. 10 minut) oraz nie mogą się powtarzać jednego dnia.
"""


import requests
import json
import random

mass = int(input("enter how much you weigh in kg: "))
height = int(input("enter how tall you are in cm: "))
age = int(input("enter how old are you: "))
max_time_activity = int(input("how long do you want to move in minutes, minimum 10: "))
ile_dni = int(input("For how many days do you want to have a training plan? : "))

def what_bmi():
    url = "https://fitness-calculator.p.rapidapi.com/bmi"

    querystring = {"age": age, "weight": mass, "height": height}

    headers = {
        'x-rapidapi-key': "bf66404f35mshecd7b9b3525744bp1d79a8jsna94048c27ef6",
        'x-rapidapi-host': "fitness-calculator.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    bmi_values = json.loads(response.text)
    print('Your Bmi is: ' + str(bmi_values['bmi']))
    what_bmi.bmi = bmi_values['bmi']
    what_bmi.health = bmi_values['health']
    what_bmi.healthy_bmi_range = bmi_values['healthy_bmi_range']
    pass


what_bmi()

def time_due_bmi(bmi):
    if max_time_activity < 10:
        print(f"minimal time activity is 10 you entered: {max_time_activity}")
    if bmi < 16:
        time = random.randint(10, max_time_activity)
    elif bmi >= 16 and bmi <= 16.9:
        time = random.randint(15, max_time_activity)
    elif bmi >= 17 and bmi <= 18.5:
        time = random.randint(20, max_time_activity)
    elif bmi >= 18.5 and bmi <= 24.9:
        time = random.randint(25, max_time_activity)
    elif bmi >= 25 and bmi <= 29.9:
        time = random.randint(30, max_time_activity)
    else:
        time = str(random.randint(30, max_time_activity))
    return time


def random_activity():
    list_activities = ['Walking/running', 'Dance', 'Build your own workout.', 'Frisbee', "Walking"]
    return random.choice(list_activities)

def create_plan():
    trening_file = open("plan.txt", "w+")
    for i in range(1, ile_dni + 1):
        trening_file.write(f'This is yor traning for day: {i} do the activity: {random_activity()} for: {time_due_bmi(what_bmi.bmi)} minutes. \n ')
    print(f'Your plan for {ile_dni} has been created check it :) ')

create_plan()