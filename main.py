import requests
import tkinter as tk

# Function to retrieve weather data from OpenWeatherMap API
def get_weather(city):
    api_key = 'b4458723386616a33859cfabde55a9ce'  # Get your API key from https://home.openweathermap.org/users/sign_up
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

# Function to update weather information displayed on the GUI
def update_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    if weather_data['cod'] == 200:  # Checking if the request was successful
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        # Update weather label with retrieved information
        weather_label.config(text=f'{description}\nTemperature: {temperature}°C\nHumidity: {humidity}%')
    else:
        # Display error message if city is not found
        weather_label.config(text="City not found")

# Creating the main application window
app = tk.Tk()
app.title("Weather App")

# Creating label and entry for user to input city
city_label = tk.Label(app, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

# Creating button to trigger weather update
get_weather_button = tk.Button(app, text="Get Weather", command=update_weather, font=('Helvetica', 14))
get_weather_button.pack()

# Creating label to display weather information
weather_label = tk.Label(app, text="")
weather_label.pack()

# Running the application
app.mainloop()
