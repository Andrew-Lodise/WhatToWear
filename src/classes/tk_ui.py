import tkinter as tk
from tkinter import ttk
from classes.outfit_recommender import OutfitRecommender
from classes.weatherman import WeatherMan
from classes.csv_panda import CsvPanda

class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("What to Wear")
        self.geometry("1000x800")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, OutfitsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        
        self.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        self.bg_color="#42ecf5"

        # setup tk variables that change in real time
        self.city_searched = tk.StringVar()
        self.weather_output = tk.StringVar()
        self.clothing_rec = tk.StringVar()
        self.source = tk.StringVar(value=1)
        self.weather_man = None

        tk.Frame.__init__(self, parent, bg=self.bg_color)

        what_to_wear_label = tk.Label(
            self, 
            text="What to Wear", 
            background=self.bg_color,
            foreground="black",
            font=("Arial Bold ", 36)
            ).pack(pady=15)
        
        # frame widget to place "get city" input and label
        questionair_frame = tk.Frame(self, bg=self.bg_color)
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
            self,
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
        update_clothing_button = tk.Button(
            output_frame,
            text = "Generate What to Wear",
            font = ("Arial", 24),
            command = self.update_clothing_rec
            ).grid(pady=10, row=0, column=1, padx=15)

        # label widget that displays the outfit info 
        self.weather_info = tk.Label(
            output_frame,
            textvariable = self.clothing_rec,
            font = ("Arial", 18),
            background=self.bg_color,
            foreground="black"
        ).grid(row=1, column=1, padx=15)


        outfits_button = tk.Button(
            self,
            text = "Edit outfits",
            font = ("Arial", 24),
            command=lambda: controller.show_frame(OutfitsPage)
            ).pack(side="right",anchor="sw", padx=15, pady=15)
        
        close_button = tk.Button(
            self,
            text = "Exit",
            font = ("Arial", 24),
            command=lambda: controller.destroy()
            ).pack(side="left",anchor="se", padx=15, pady=15)
    
    def update_weather_output(self, event=None):
        city = self.city_searched.get()
        
        if not city:
            self.weather_man = None
            self.weather_output.set("Error: Enter a city in the box above")
        else:
            try:
                self.weather_man = WeatherMan(city, int(self.source.get()))
                
                self.weather_output.set(self.weather_man.output)
                self.bg_color = "#ffffff"
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


class OutfitsPage(tk.Frame):
    def __init__(self, parent, controller):
        self.bg_color="#42e0f0"
        self.outfits = OutfitRecommender().outfit_list

        # setup tk variables that change in real time

        tk.Frame.__init__(self, parent, bg=self.bg_color)

        title_label = tk.Label(
            self, 
            text="Outfits", 
            background=self.bg_color,
            foreground="black",
            font=("Arial Bold ", 36)
            ).pack(pady=15)
        
        outfit_table_frame = tk.Frame(self, bg="black", width=800, height=500)
        outfit_table_frame.pack(pady=10, padx=15)

        cols = ["Head", "Torso", "Leg", "Foot", "High", "Low"]
        tree = ttk.Treeview(outfit_table_frame, columns=cols, show='headings')

        for col in cols:
            tree.heading(col, text=col, anchor="center")
            tree.column(col, width=(150))

        # Set font size
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial Bold', 18))  # Adjust the font size here
        style.configure("Treeview", font=('Arial', 14))  # Adjust the font size here

        # Configure row styles
        tree.tag_configure('oddrow', background='#E8E8E8')
        tree.tag_configure('evenrow', background='white')
        
        # populate table
        for i, outfit in enumerate(self.outfits):
            tags = 'evenrow' if i % 2 == 0 else 'oddrow'
            tree.insert("", "end", values=outfit.get_list(), tags=tags)


        tree.grid(row=0, column=0)
        
        home_button = tk.Button(
            self,
            text = "Back to home",
            font = ("Arial", 24),
            command=lambda: controller.show_frame(StartPage)
            ).pack(side="right",anchor="se", padx=15, pady=15)
        
        close_button = tk.Button(
            self,
            text = "Exit",
            font = ("Arial", 24),
            command=lambda: controller.destroy()
            ).pack(side="left",anchor="sw", padx=15, pady=15)
        
        