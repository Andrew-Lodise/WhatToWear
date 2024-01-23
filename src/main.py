from classes.email_sender import EmailSender
from classes.outfit_recommender import OutfitRecommender
from classes.weatherman import WeatherMan
from classes.tk_ui import Tk_ui


def main():

    wm = WeatherMan(city="Secane", source=1)
    #os = OutfitRecommender()
    #temp = wm.get_target()
    email_sender = EmailSender([wm.output, "para2"]) #os.recommendation

    # test the ui
    gotk = Tk_ui()

    # to manipulate csv
    #m.run() #✔

    # to setup what to wear
    #print(email_sender.body) #✔
    #email_sender.send_email() #✔



if __name__ == "__main__":
    main()