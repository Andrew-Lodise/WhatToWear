import requests

# key 2490a629b8ce54df289dfef48798119a
api_key = "2490a629b8ce54df289dfef48798119a"

city = "Philadelphia"

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
)

if weather_data.json()["cod"] == 404:
    print("No city found.")

else:
    pass
    # print(weather_data.json()["weather"])
    # print(weather_data.json()["main"])
    # print(weather_data.json()["wind"])
    # print(weather_data.json())
