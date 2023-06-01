from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests
url_api = " https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

#api_key = '8d50a70ad52c4813eb5009756b8673c9'
api_file='weather.key'
file_a= ConfigParser()
file_a.read(api_file)
api_key = file_a['api_key']['key']

def weather_find(city):
    final = requests.get(url_api.format(city,api_key))
    if final:
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        k_temperature = json_file["main"]['temp']
        c_temperature = k_temperature-273.15
        f_temperature = (k_temperature-273.15)*9/5+32
        weather_display = json_file['weather'][0]['main']
        result = (city,country_name,c_temperature,f_temperature,weather_display)

        return result
    else:
        return None

def print_weather():
    city = search_city.get()
    weather = weather_find(city)
    if weather:
        location_entry['text'] = '{}, {}'.format(weather[0], weather[1])
        temperature_entry['text'] = '{:.2f} C , {:.2f} F'.format(weather[2] , weather[3])
        weather_entry['text'] = weather[4]

    else:
        messagebox.showerror('Error' , 'Please enter valid city')



root = Tk()
root.title("WEATHER FORECAST API")
bg = PhotoImage(file = "R.png")
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

root.geometry("550x400")

search_city = StringVar()
enter_city = Entry(root , textvariable= search_city , justify=CENTER,  fg="black" , font=("Arial",30,"bold"))
enter_city.pack()

search_button = Button(root, text='SEARCH WEATHER', justify=CENTER, width=20 , background="white" , font=("Arial" , 25 , "bold"), command=print_weather)
search_button.pack()

location_entry = Label(root, text = 'Location:' , font = ("Arial" , 35 , "bold") , bg="lightblue")
location_entry.pack(pady= 10)

temperature_entry = Label(root, text='Temperature:')
temperature_entry.pack(pady=10)

weather_entry = Label(root, text= 'Condition' , font=("Arial" , 35 , "bold"), bg="lightblue")
weather_entry.pack(pady= 10)

root.mainloop()