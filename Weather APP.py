import tkinter as tk
import requests
import json


def fetch_weather():
    city = city_entry.get()
    api_key = "26d63df035dd7d7e87cefe5a34f8cbdb"  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()

        if response.status_code == 200:
            weather_desc = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            result_text = f"Weather in {city}:\n"
            result_text += f"Description: {weather_desc}\n"
            result_text += f"Temperature: {temperature}°C\n"
            result_text += f"Humidity: {humidity}%\n"
            result_text += f"Wind Speed: {wind_speed} m/s"

            result_label.config(text=result_text)
        else:
            result_label.config(text=f"Error: {data['message']}")

    except Exception as ex:
        result_label.config(text=f"Error fetching weather data: {ex}")


# Create the main application window
root = tk.Tk()
root.title("Weather App")

# Create GUI widgets
label = tk.Label(root, text="Enter city name:")
label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
