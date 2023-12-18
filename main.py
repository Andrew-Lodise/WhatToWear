from weather_man import WeatherMan
from email_messenger import EmailMessenger
from clothing_recommender import ClothingRecommender


def main():

    philly_weatherman = WeatherMan(city="Secane")
    #print(philly_weatherman.output) #✔
    #philly_weatherman.print_weather_output() #✔
    #print(philly_weatherman.weather_data)

    my_clothing_ai = ClothingRecommender(philly_weatherman.weather_data)
    #print(my_clothing_ai.recommendation) #✔
    #my_clothing_ai.print_recommendation() #✔
    
    my_mailman = EmailMessenger(philly_weatherman.output, my_clothing_ai.recommendation)
    #print(my_mailman.body) #✔
    my_mailman.print_email() #✔
    #my_mailman.send_email() #✔

if __name__ == "__main__":
    main()
