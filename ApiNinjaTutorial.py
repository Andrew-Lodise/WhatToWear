import requests

def get_weather(city):
    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

    querystring = {"city":city}

    headers = {
        "X-RapidAPI-Key": "a6c17e5754msh648ccd5c56023d5p13a1a5jsnfced0c3bf00d",
        "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

x = get_weather("Philadelphia")
print(x)