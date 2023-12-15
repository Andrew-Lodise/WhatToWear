from weather_man import WeatherMan
from email_messenger import EmailMessenger


def main():

    philly_weatherman = WeatherMan(city="Philadelphia")
    philly_weatherman.print_weather_data() 
    EmailMessenger.send_email(philly_weatherman.output)

if __name__ == "__main__":
    main()
