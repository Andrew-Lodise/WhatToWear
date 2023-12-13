from WebScrapeWeather import get_weather
from TextingTutorial import email_alert


def main():

    city = "Philadelphia"
    wd = get_weather(city) # wd = weather data

    print(wd['msg'])
    email_alert(wd['msg'])

main()
