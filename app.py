import requests
from tkinter import *

# Replace with your own OpenWeatherMap API key
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        result = (
            f"City: {city}\n"
            f"Temperature: {main['temp']}°C\n"
            f"Humidity: {main['humidity']}%\n"
            f"Condition: {weather['description'].title()}"
        )
    else:
        result = "City not found. Please try again."
    return result

def show_weather():
    city = city_entry.get()
    weather_info = get_weather(city)
    result_label.config(text=weather_info)

# GUI setup
app = Tk()
app.title("Weather App")
app.geometry("300x250")

city_label = Label(app, text="Enter City Name:", font=("Arial", 12))
city_label.pack(pady=10)

city_entry = Entry(app, width=25)
city_entry.pack()

search_button = Button(app, text="Get Weather", command=show_weather)
search_button.pack(pady=10)

result_label = Label(app, text="", font=("Arial", 11), justify=LEFT)
result_label.pack(pady=10)

app.mainloop()


