from classes.email_sender import EmailSender
from classes.menu import Menu
from classes.outfit_recommender import OutfitRecommender
from classes.weatherman import WeatherMan


def main():

    weatherman = WeatherMan()
    os = OutfitRecommender(weatherman.target)
    email_sender = EmailSender([weatherman.output, os.recommendation])
    m = Menu()

    # to manipulate csv
    #m.run() #✔

    # to setup what to wear
    #print(email_sender.body) #✔
    #email_sender.send_email() #✔



if __name__ == "__main__":
    main()