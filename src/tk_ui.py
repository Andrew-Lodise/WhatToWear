import tkinter as tk
from classes.weatherman import WeatherMan

class tk_ui:
    def __init__(self):

        #setup the root
        self.root = tk.Tk()
        self.root.title("What to Wear")
        self.bg_color = "#42ecf5"

        # setup tk variables that change in real time
        self.city = tk.StringVar()
        self.weather_output = tk.StringVar()
        
        #running the tkinter object
        self.frame1()
        self.root.mainloop()

    def update_weather_info(self):
        city = self.city.get()
        try:
            s = WeatherMan(city)
            self.weather_output.set(s.output)
        except IndexError as e:
            self.weather_output.set("Error: location no found")
        

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
        self.mainframe.pack_propagate(False)

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
        entry_row.pack()

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
            textvariable=self.city,
            font=("Arial", 16),
            background="white",
            foreground="black")
        city_entry.grid(row=0, column=1, pady=5)
        city_entry.focus_set()
        
        # button widget to "generate the weather data"
        generate_weather_info_button = tk.Button(
            self.mainframe,
            text = "Generate weather data",
            font = ("Arial", 24),
            command = self.update_weather_info
            ).pack(pady=5)
        
        # label that displays the weather info
        self.weather_info = tk.Label(
            self.mainframe,
            textvariable = self.weather_output,
            font = ("Arial", 18),
            background=self.bg_color,
            foreground="black"
        ).pack(pady=5)


tk_ui()