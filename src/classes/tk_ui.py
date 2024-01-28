import tkinter as tk
from classes.weatherman import WeatherMan
from classes.outfit_recommender import OutfitRecommender

class Tk_ui:
    def __init__(self):
        #setup the root
        self.root = tk.Tk()
        self.root.title("What to Wear")
        self.bg_color = "#42ecf5"

        # setup tk variables that change in real time
        self.city_searched = tk.StringVar()
        self.weather_output = tk.StringVar()
        self.clothing_rec = tk.StringVar()
        self.source = tk.StringVar(value=1)
        self.weather_man = None
        
        #running the tkinter object
        self.frame1()
        self.root.mainloop()


    def update_weather_output(self, event=None):
        city = self.city_searched.get()
        
        if not city:
            self.weather_man = None
            self.weather_output.set("Error: Enter a city in the box above")
        else:
            try:
                self.weather_man = WeatherMan(city, int(self.source.get()))
                
                self.weather_output.set(self.weather_man.output)
            except (KeyError, IndexError):
                self.weather_man = None
                self.weather_output.set("Error: Unknown city")
            

    def update_clothing_rec(self):
        if self.weather_man != None:
            self.outfit_recommender = OutfitRecommender()
            self.outfit_recommender.set_temp(self.weather_man.get_target())
            self.clothing_rec.set(self.outfit_recommender.recommendation) 
        else:
            self.clothing_rec.set("Error: provide weather info first")


    def frame1(self):
        # frame widget for the main ui
        self.mainframe = tk.Frame(
            self.root, 
            padx=3, 
            pady=12, 
            width=1000, 
            height= 800, 
            bg=self.bg_color)
        
        self.mainframe.pack()
        self.mainframe.pack_propagate(False)

        # label widget for the title of the ui
        what_to_wear_label = tk.Label(
            self.mainframe, 
            text="What to Wear", 
            background=self.bg_color,
            foreground="black",
            font=("Arial Bold ", 36)
            ).pack(pady=5)

        # frame widget to place "get city" input and label
        questionair_frame = tk.Frame(self.mainframe, bg=self.bg_color)
        questionair_frame.pack(pady=10)

        # label to tell user to "enter city"
        instruction_label = tk.Label(
            questionair_frame,
            text = "Enter city: ",
            background=self.bg_color,
            foreground="black",
            font=("Arial", 24)
        ).grid(row=0, column=0)

        # entry widget to capture city
        city_entry = tk.Entry(
            questionair_frame,
            textvariable=self.city_searched,
            font=("Arial", 24),
            background="white",
            insertbackground="black",
            foreground="black")
        city_entry.grid(row=0, column=1)
        city_entry.bind("<Return>", self.update_weather_output)
        city_entry.focus_set()

        # frame widget to place radio buttons for source
        source_selection = tk.Frame(
            questionair_frame,
            bg=self.bg_color)
        source_selection.grid(row=0, column=2)
        # radio button widget for api
        api_radio = tk.Radiobutton(
            source_selection,
            text="Open Weather Map API", 
            font = ("Arial", 20),
            variable=self.source,
            background = self.bg_color, 
            foreground = "black",
            value=0).grid(row=0, column=0, sticky=tk.W, padx=15)
        # radio button widget for web scrape
        web_radio = tk.Radiobutton(
            source_selection, 
            text="Google Web Scrape", 
            font = ("Arial", 20),
            variable=self.source,
            background = self.bg_color, 
            foreground = "black",
            value=1).grid(row=1, column=0, sticky=tk.W, padx=15)
        # frame widget to place weather and clothing buttons and outputs
        output_frame = tk.Frame(
            self.mainframe,
            background=self.bg_color)
        output_frame.pack(pady=10)
        # button widget to "generate the weather data"
        generate_weather_info_button = tk.Button(
            output_frame,
            text = "Generate weather data",
            font = ("Arial", 24),
            command = self.update_weather_output
            ).grid(pady=10, row=0, column=0, padx=15)

        # label widget that displays the weather info
        self.weather_info = tk.Label(
            output_frame,
            textvariable = self.weather_output,
            font = ("Arial", 18),
            background=self.bg_color,
            foreground="black"
        ).grid(row=1, column=0, padx=15)

            # button widget to "generate the weather data"
        test_button = tk.Button(
            output_frame,
            text = "Generate What to Wear",
            font = ("Arial", 24),
            command = self.update_clothing_rec
            ).grid(pady=10, row=0, column=1, padx=15)

        # label widget that displays the weather info
        self.weather_info = tk.Label(
            output_frame,
            textvariable = self.clothing_rec,
            font = ("Arial", 18),
            background=self.bg_color,
            foreground="black"
        ).grid(row=1, column=1, padx=15)