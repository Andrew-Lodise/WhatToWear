from WebScrapeWeather import get_weather
from TextingTutorial import email_alert


def main():

    city = "Philadelphia"
    wd = get_weather(city) # wd = weather data
    msg = f'''Today is {wd['temp']}{wd['unit']} and {wd['desc']}.
    \nThe high is {wd['high']}{wd['unit']} and the low is {wd['low']}{wd['unit']}.
    \nPercipitation:{wd['percip']} Humidity:{wd['humid']} Wind Speed:{wd['wind']}'''

    print(msg)
    email_alert(msg)

main()
