from WeatherTutorial import get_weather_data, get_info
from TextingTutorial import email_alert


def main():

    city = "Philadelphia"
    weather_data = get_weather_data(city)
    data = get_info(weather_data)
    msg = f"Today is {data[0]}, with a high of {data[3]} and low of {data[3]}."
    email_alert(msg)


main()
