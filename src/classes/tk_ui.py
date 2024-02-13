import tkinter as tk
from tkinter import ttk
from classes.outfit_recommender import OutfitRecommender
from classes.weatherman import WeatherMan
from classes.csv_panda import CsvPanda
import os

# Get the full path to the custom font file
custom_font_path = "ProtestRevolution-Regular.ttf" 
custom_font = ("Helvetica", 32)

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
            background="gray",
            foreground="black",
            width=30,
            heigh=15
        ).grid(row=1, column=0, padx=15)

            # button widget to "generate the weather data"
        update_clothing_button = tk.Button(
            output_frame,
            text = "Generate Outfit",
            font = ("Arial", 24),
            command = self.update_clothing_rec
            ).grid(pady=10, row=0, column=1, padx=15)

        # label widget that displays the outfit info 
        self.weather_info = tk.Label(
            output_frame,
            textvariable = self.clothing_rec,
            font = ("Arial", 18),
            background="gray",
            foreground="black",
            width=30,
            height=15,
            
            
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
        self.outfit_recommender = OutfitRecommender()
        self.outfits = self.outfit_recommender.outfit_list

        # setup tk variables that change in real time
        self.head_entry_text = tk.StringVar()
        self.torso_entry_text = tk.StringVar()
        self.leg_entry_text = tk.StringVar()
        self.foot_entry_text = tk.StringVar()
        self.high_entry_text = tk.StringVar()
        self.low_entry_text = tk.StringVar()
        self.error_output = tk.StringVar()
        self.removal_index = tk.StringVar()

        tk.Frame.__init__(
            self, 
            parent, 
            bg=self.bg_color,
            )
        self.grid()

        title_label = tk.Label(
            self, 
            text="Outfits", 
            background=self.bg_color,
            foreground="black",
            font=("Arial Bold", 36)
            ).pack(pady=15)
        
        self.outfit_table_frame = tk.Frame(self, bg="blue", width=1000)
        self.outfit_table_frame.pack(pady=10, padx=15)

        self.cols = ["Head", "Torso", "Leg", "Foot", "High", "Low"]
        self.tree = ttk.Treeview(self.outfit_table_frame, columns=self.cols, show='headings', height=len(self.outfits))

        for col in self.cols:
            self.tree.heading(col, text=col, anchor="w")
            self.tree.column(col, width=(1000//6), minwidth=150, stretch=False)
        
        # Additionally, configure the parent frame of the Treeview widget to prevent column resizing:
        self.outfit_table_frame.grid_columnconfigure(0, weight=1)  # Ensure the first (and only) column of the outfit_table_frame widget has a weight of 1

        # Set font size
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(custom_font, 18), foreground="black")  # Adjust the font size here
        style.configure("Treeview", font=('Arial', 12), foreground="black")  # Adjust the font size here

        # Configure row styles
        self.tree.tag_configure('oddrow', background='#E8E8E8')
        self.tree.tag_configure('evenrow', background='white')
        
        # populate table
        for i, outfit in enumerate(self.outfits):
            tags = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tree.insert("", "end", values=outfit.get_list(), tags=tags)

        self.tree.grid(row=0, column=0)
        
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

        Add_user_label = tk.Label(
            self,
            background=self.bg_color,
            font=("Times New Roman", 30),
            text="Add Outfit Here↓"
        ).pack()

        form_bg = "lightblue"
        form_frame = tk.Frame(
            self,
            background=form_bg,
            width=200
        )
        form_frame.pack(padx=0)

        # labels and entries for the form to add a new user
        label_font = ("Arial", 18)
        entry_font = ("Times New Roman", 14)
        head_label = tk.Label(
            form_frame,
            text="Head:",
            font=label_font,
            background=form_bg
        ).grid(row=0, column=0)

        head_entry = tk.Entry(
            form_frame,
            font=entry_font,
            textvariable=self.head_entry_text
        ).grid(row=1, column=0, padx=5, pady=5)

        torso_label = tk.Label(
            form_frame,
            text="Torso:",
            font=label_font,
            background=form_bg
        ).grid(row=0, column=1)

        torso_entry = tk.Entry(
            form_frame,
            font=entry_font,
            textvariable=self.torso_entry_text
        ).grid(row=1, column=1, padx=5, pady=5)

        leg_label = tk.Label(
            form_frame,
            text="Leg:",
            font=label_font,
            background=form_bg
        ).grid(row=0, column=2)

        leg_entry = tk.Entry(
            form_frame,
            font=entry_font,
            textvariable=self.leg_entry_text
        ).grid(row=1, column=2, padx=5, pady=5)
        
        foot_label = tk.Label(
            form_frame,
            text="Foot:",
            font=label_font,
            background=form_bg
        ).grid(row=2, column=0)

        foot_entry = tk.Entry(
            form_frame,
            font=entry_font,
            textvariable=self.foot_entry_text
        ).grid(row=3, column=0, padx=5, pady=5)

        high_label = tk.Label(
            form_frame,
            text="High:",
            font=label_font,
            background=form_bg
        ).grid(row=2, column=1)

        high_entry = tk.Entry(
            form_frame,
            font=entry_font,
            textvariable=self.high_entry_text
        ).grid(row=3, column=1, padx=5, pady=5)

        low_label = tk.Label(
            form_frame,
            text="Low:",
            font=label_font,
            background=form_bg
        ).grid(row=2, column=2)

        low_entry = tk.Entry(
            form_frame,
            font=entry_font,
            textvariable=self.low_entry_text
        ).grid(row=3, column=2, padx=5)

        submit_buttom = ttk.Button(
            form_frame,
            text="Submit",
            command=self.add_outfit_to_csv
        ).grid(row=5, column=1)

        error_label = tk.Label(
            self,
            textvariable=self.error_output,
            font=("Arial", 14),
            background=self.bg_color
        )
        error_label.pack()

        delete_user_label = tk.Label(
            self,
            background=self.bg_color,
            font=("Times New Roman", 30),
            text="Delete Outfit Here↓"
        ).pack()
        
        delete_frame = tk.Frame(
            self,
            background="lightgreen"
        )
        delete_frame.pack()

        delete_outfit_label = tk.Label(
            delete_frame,
            background="lightgreen",
            text="Enter the entry number below",
            font=label_font
        ).pack()
    
        delete_index_entry = tk.Entry(
            delete_frame,
            font=entry_font,
            textvariable=self.removal_index
        ).pack()

        submit_buttom = ttk.Button(
            delete_frame,
            text="Submit",
            command=self.remove_outfit_from_csv
        ).pack()

    def remove_outfit_from_csv(self):
        try:
            index = int(self.removal_index.get()) - 1
            self.outfit_recommender.cp.delete_row(index)
            self.repopulate_table()
            self.removal_index.set(value="")
        except Exception as e:
            print("Error: make sure a number is in the field above")

    def add_outfit_to_csv(self):
        try:
            head = self.head_entry_text.get()
            torso = self.torso_entry_text.get()
            leg = self.leg_entry_text.get()
            foot = self.foot_entry_text.get()
            high = self.high_entry_text.get()
            low = self.low_entry_text.get()

            row = [head, torso, leg, foot, float(high), float(low)]
            self.outfit_recommender.cp.add_row(row)
            self.repopulate_table()
            self.error_output.set("Outfit Added.")
            self.head_entry_text.set("")
            self.torso_entry_text.set("")
            self.leg_entry_text.set("")
            self.foot_entry_text.set("")
            self.high_entry_text.set("")
            self.low_entry_text.set("")

        except ValueError as e:
            self.error_output.set("Error: fill in all fields.\nMake sure high and low are numbers")
            print(f"error: {e}")

    def repopulate_table(self):
        # Clear existing items from the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.outfit_recommender = OutfitRecommender()
        self.outfits = self.outfit_recommender.outfit_list
        

        self.cols = ["Head", "Torso", "Leg", "Foot", "High", "Low"]
        if self.removal_index.get() == "":
            self.tree = ttk.Treeview(self.outfit_table_frame, columns=self.cols, show='headings', height=len(self.outfits))

        for col in self.cols:
            self.tree.heading(col, text=col, anchor="w")
            self.tree.column(col, width=(1000//6), minwidth=150, stretch=False)

        # Additionally, configure the parent frame of the Treeview widget to prevent column resizing:
        self.outfit_table_frame.grid_columnconfigure(0, weight=1)  # Ensure the first (and only) column of the outfit_table_frame widget has a weight of 1

        # Set font size
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(custom_font, 18), foreground="black")  # Adjust the font size here
        style.configure("Treeview", font=('Arial', 12), foreground="black")  # Adjust the font size here

        # Configure row styles
        self.tree.tag_configure('oddrow', background='#E8E8E8')
        self.tree.tag_configure('evenrow', background='white')

        # populate table
        for i, outfit in enumerate(self.outfits):
            tags = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tree.insert("", "end", values=outfit.get_list(), tags=tags)

        self.tree.grid(row=0, column=0)
        