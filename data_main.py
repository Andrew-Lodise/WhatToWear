from weather_recorder import WeatherRecorder 

def main():
    secretary = WeatherRecorder("data/data.csv", "data/data_copy.xlsx")
    #print(secretary.df)

    #secretary.add_row(WeatherRecorder.example_data) #✔
    #print(secretary.df)
    #secretary.save_file() #✔

    #secretary.ask_user()


if __name__ == "__main__":
    main()
