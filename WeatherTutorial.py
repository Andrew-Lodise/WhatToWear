import requests


def get_weather_data(city):

    api_key = "2490a629b8ce54df289dfef48798119a"

    city = city

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
    )

    if weather_data.json()["cod"] == 404:
        print("No city found.")

    return weather_data.json()


# outputs data from weather data, might make it a dictionary later
def get_info(wd):
    desc = wd["weather"][0]["description"]
    cur_temp = wd["main"]["temp"]
    cur_feel = wd["main"]["feels_like"]
    high = wd["main"]["temp_max"]
    low = wd["main"]["temp_min"]
    humid = wd["main"]["humidity"]
    wind_speed = wd["wind"]["speed"]
    return [desc, cur_temp, cur_feel, high, low, humid, wind_speed]
