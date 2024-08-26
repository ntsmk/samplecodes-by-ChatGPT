import requests


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()


def display_weather(weather_data):
    if weather_data.get('cod') != 200:
        print("City not found!")
        return

    city = weather_data['name']
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")


def main():
    api_key = 'API'
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
