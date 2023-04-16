from WeatherTutorial import get_weather_data, get_info
from TextingTutorial import email_alert


def main():

    city = "Philadelphia"
    weather_data = get_weather_data(city)
    data = get_info(weather_data)
    msg = f"Today is {data['desc']}, with a high of {round(data['high'])} and low of {round(data['low'])}."
    email_alert(msg)
    print(msg)


main()
