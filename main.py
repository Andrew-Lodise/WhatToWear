from weather_man import WeatherMan
from email_messenger import EmailMessenger
from clothing_recommender import ClothingRecommender


def main():
    philly_weatherman = WeatherMan() # gets location and source from config file
    #philly_weatherman.get_api_weather_data()
    #print(philly_weatherman.output) #✔
    #philly_weatherman.print_weather_output() #✔
    #print(philly_weatherman.weather_data) #✔
    #philly_weatherman.read_config() #✔

    my_clothing_ai = ClothingRecommender(weather_data=philly_weatherman.weather_data)
    #print(my_clothing_ai.recommendation) #✔
    #my_clothing_ai.print_recommendation() #✔
    
    my_mailman = EmailMessenger(weather_output=philly_weatherman.output, 
                                recommendation=my_clothing_ai.recommendation)
    #print(my_mailman.body) #✔
    my_mailman.print_email() #✔
    my_mailman.send_email() #✔ #

if __name__ == "__main__":
    main()
