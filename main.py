from clothing_recommender import ClothingRecommender
from email_messenger import EmailMessenger
from weatherman import Weatherman

def main():

    #main method contents
    philly_weatherman = Weatherman() # gets location and source from config file
    my_clothing_ai = ClothingRecommender(philly_weatherman)
    my_emailman = EmailMessenger(philly_weatherman, my_clothing_ai) 
    
    # WeatherMan tests
    #philly_weatherman.get_api_weather_data()
    #print(philly_weatherman.output) #✔
    #philly_weatherman.print_weather_output() #✔
    #print(philly_weatherman.weather_data) #✔
    #philly_weatherman.read_config() #✔

    # ClothingReccomender tests
    #print(my_clothing_ai.recommendation) #✔
    #my_clothing_ai.print_recommendation() #✔
    
    # EmailMessenger tests
    #print(my_mailman.body) #✔
    my_emailman.print_email() #✔
    #my_mailman.send_email() #✔ 

if __name__ == "__main__":
    main()
