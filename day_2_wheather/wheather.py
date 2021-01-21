import random
import tkinter as tk
import json
import requests
from PIL import ImageTk, Image
from datetime import datetime

#parameters to wheter check


url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"Warsaw,pl","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

headers = {
    'x-rapidapi-key': "bf66404f35mshecd7b9b3525744bp1d79a8jsna94048c27ef6",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

#screen size

HEIGHT = 575
WIDTH = 960

# parameters to random quotes

url_quotes = 'https://type.fit/api/quotes'

def random_quotes():
    response = requests.request("GET", url_quotes)
    json_pars = json.loads(response.text)
    random_number = random.randint(1,1000)
    random_quotes.text = json_pars[random_number]['text']
    random_quotes.autor = json_pars[random_number]['author']




def data_wheather():
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    json_to_pars = json.loads(response.text[5:-1])
    data_wheather.weather = json_to_pars['weather'][0]['main']
    data_wheather.temp = "{:.2f}".format((int(json_to_pars['main']['temp']) - 273.15))
    data_wheather.pressure = json_to_pars['main']['pressure']
    data_wheather.dt = datetime.fromtimestamp(int(json_to_pars['dt'])).strftime("%A, %B %d, %Y %I:%M:%S")



def insert_data():
    data_wheather()
    random_quotes()
    jaka_pogoda.insert(tk.INSERT, "Weather: " + data_wheather.weather + "\n")
    jaka_pogoda.insert(tk.INSERT, "Temp: " + str(data_wheather.temp)+ "\n")
    jaka_pogoda.insert(tk.INSERT, "Pressure: " + str(data_wheather.pressure)+ "\n")
    jaka_pogoda.insert(tk.INSERT, "Date: " + data_wheather.dt + "\n")
    jaka_pogoda.insert(tk.INSERT, "Quotation: " + random_quotes.text + "\n")
    jaka_pogoda.insert(tk.INSERT, "Author: " + random_quotes.autor + "\n")




root = tk.Tk()

root.title("weather")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, background="#C9F6CD")

frame.place(relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("globus.jpg"))

label = tk.Label(frame, image=img)
label.pack()

miasto = tk.Entry(frame, bd="3")
miasto.place(relheight=0.05, relwidth=0.3, relx=0.4, rely=0.1)

jaka_pogoda = tk.Text(frame)
jaka_pogoda.config(state="normal")
jaka_pogoda.place(relheight=0.3, relwidth=0.4, relx=0.4, rely=0.3)

button = tk.Button(frame, text="Check", bd="3", command=lambda: insert_data())
button.place(relheight=0.05, relwidth=0.1, relx=0.1, rely=0.1)


root.mainloop()




