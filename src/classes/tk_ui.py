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
        self.source = tk.StringVar(value=0)
        self.clothing_rec = tk.StringVar()
        
        #running the tkinter object
        self.frame1()
        self.root.mainloop()

    def update_weather_output(self):
        city = self.city_searched.get()
        try:
            if not city:
                self.weather_output.set("Error: Enter a city in the box above")
            else:
                self.weather_man = WeatherMan(city, int(self.source.get()))
                self.weather_output.set(self.weather_man.output)
        except (IndexError, AttributeError) as e:
            self.weather_output.set("Error: location not found")

    def update_what_to_wear(self):
        try:
            self.recommender = OutfitRecommender()
            self.recommender.set_temp(self.weather_man.target)
            self.clothing_rec.set(self.recommender.recommendation)
        except AttributeError as e:
            self.clothing_rec.set("Error: Must generate weather first")

    def frame1(self):
        # frame widget for the main ui
        self.mainframe = tk.Frame(
            self.root, 
            padx=3, 
            pady=12, 
            width=400, 
            height= 400, 
            bg=self.bg_color)
        
        self.mainframe.pack()
        #self.mainframe.pack_propagate(False)

        # label widget for the title of the ui
        what_to_wear_label = tk.Label(
            self.mainframe, 
            text="What to Wear", 
            background=self.bg_color,
            foreground="black",
            font=("Arial Bold ", 26)
            ).pack(pady=5)

        # frame widget to place get city input and label
        entry_row = tk.Frame(self.mainframe, bg=self.bg_color)
        entry_row.pack(pady=10)

        # label to tell user to "enter city"
        instruction_label = tk.Label(
            entry_row,
            text = "Enter city: ",
            background=self.bg_color,
            foreground="black",
            font=("Arial", 20)
        ).grid(row=0, column=0)

        # entry widget to capture city
        city_entry = tk.Entry(
            entry_row,
            textvariable=self.city_searched,
            font=("Arial", 16),
            background="white",
            foreground="black")
        city_entry.grid(row=0, column=1)
        city_entry.focus_set()

        # frame widget to place radio buttons for source
        source_selection = tk.Frame(
            self.mainframe,
            bg=self.bg_color)
        source_selection.pack(pady=10)
        # radio button widget for api
        api_radio = tk.Radiobutton(
            source_selection,
            text="Open Weather Map API", 
            font = ("Arial", 16),
            variable=self.source,
            background = self.bg_color, 
            foreground = "black",
            value=0).grid(row=0, column=0)
        # radio button widget for web scrape
        web_radio = tk.Radiobutton(
            source_selection, 
            text="Google Web Scrape", 
            font = ("Arial", 16),
            variable=self.source,
            background = self.bg_color, 
            foreground = "black",
            value=1).grid(row=0, column=1)
        
        # button widget to "generate the weather data"
        generate_weather_info_button = tk.Button(
            self.mainframe,
            text = "Generate weather data",
            font = ("Arial", 20),
            command = self.update_weather_output
            ).pack(pady=10)
        
        # label widget that displays the weather info
        self.weather_info = tk.Label(
            self.mainframe,
            textvariable = self.weather_output,
            font = ("Arial", 18),
            background=self.bg_color,
            foreground="black"
        ).pack(pady=10)

        # button widget for "Generate What to Wear"

        generate_what_to_wear_button = tk.Button(
            self.mainframe,
            text = "Generate what to wear",
            font = ("Arial", 20),
            background=self.bg_color,
            command = self.update_what_to_wear 
            ).pack(pady=10)
        
        # label widget that displays what to wear
        self.what_to_wear_info = tk.Label(
            self.mainframe,
            textvariable = self.clothing_rec,
            font = ("Arial", 18),
            background=self.bg_color,
            foreground="black"
        ).pack(pady=10)


