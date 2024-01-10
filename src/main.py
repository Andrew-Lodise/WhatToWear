from classes.clothing_recommender import ClothingRecommender
from classes.weatherman import WeatherMan
from classes.weather_recorder import WeatherRecorder

from classes.email_sender import EmailSender

def main():

    #main method contents
    #philly_weatherman = Weatherman() # gets location and source from config file
    #my_clothing_ai = ClothingRecommender(philly_weatherman)
    #my_emailman = EmailMessenger(philly_weatherman, my_clothing_ai) 

    #weather recorder
    #secretary = WeatherRecorder("data/data.csv", "data/data_copy.xlsx")
    
    # WeatherMan tests
    #philly_weatherman.get_api_weather_data()
    #print(philly_weatherman.output) #✔
    #philly_weatherman.print_weather_output() #✔
    #print(philly_weatherman.weather_data) #✔
    #philly_weatherman.read_config() #✔
    #philly_weatherman.get_todays_date() #✔
    #print(Weatherman.get_todays_date())#✔

    # ClothingReccomender tests
    #print(my_clothing_ai.recommendation) #✔
    #my_clothing_ai.print_recommendation() #✔
    
    # EmailMessenger tests
    #print(my_mailman.body) #✔
    #my_emailman.print_email() #✔ #MAIN
    #my_mailman.send_email() #✔ 

    # DataRecorder tests
    #secretary.add_row(WeatherRecorder.example_data) #✔
    #secretary.save_file() #✔
    #secretary.ask_user() #✔
    
    #--- main after refactoring ----
    weatherman = WeatherMan() # gets location and source from config file
    clothing_recommender = ClothingRecommender(weatherman)
    email_sender = EmailSender([weatherman.output, clothing_recommender.recommendation],)

    #Email sender tests
    print(email_sender.body) #✔
    #email_sender.send_email() #✔

if __name__ == "__main__":
    main()