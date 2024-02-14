import tkinter as tk
from tkinter import ttk
from classes.outfit_recommender import OutfitRecommender
from classes.weatherman import WeatherMan

#globals
c1 = "#cee5d8" #lightest
c2 = "#b6dec8"
c3 = "#9bd3b4"
c4 = "#84c9a3"
c5 = "#72b791" #darkest
title_font = ("Courier New Bold", 36)
button_font = ("Courier New Bold", 20)
label_font = ("Courier New", 18)
entry_font = ("Times New Roman", 18)
radio_font = ("Courier New Bold", 20)
long_output_font = ("Courier New", 18)
large_lable_font = ("Courier New", 30)
medium_lable_font = ("Times New Roman", 24)

class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("What to Wear")
        self.geometry("1000x840")

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
        self.bg_color=c4

        # setup tk variables that change in real time
        self.city_searched = tk.StringVar()
        self.weather_output = tk.StringVar()
        self.clothing_rec = tk.StringVar()
        self.source = tk.StringVar(value=1) # default = google
        self.weather_man = None

        tk.Frame.__init__(self, parent, bg=self.bg_color)

        what_to_wear_label = tk.Label(
            self, 
            text="What to Wear", 
            background=c4,
            foreground="black",
            font=title_font
            ).pack(pady=15)
        
        # frame widget to place "get city" input and label
        questionair_frame = tk.Frame(self, bg=c3)
        questionair_frame.pack(pady=10)

        # label to tell user to "enter city"
        instruction_label = tk.Label(
            questionair_frame,
            text = "Enter city: ",
            background=c3,
            foreground="black",
            font=large_lable_font
        ).grid(row=0, column=0)

        # entry widget to capture city
        city_entry = tk.Entry(
            questionair_frame,
            textvariable=self.city_searched,
            font=entry_font,
            background=c1,
            foreground="black")
        city_entry.grid(row=0, column=1)
        city_entry.bind("<Return>", self.update_weather_output)
        city_entry.focus_set()

        # frame widget to place radio buttons for source
        source_selection = tk.Frame(
            questionair_frame,
            bg=c3)
        source_selection.grid(row=0, column=2)
        
        # radio button widget for api
        api_radio = tk.Radiobutton(
            source_selection,
            text="Open Weather Map API", 
            font = radio_font,
            variable=self.source,
            background = c3, 
            foreground = "black",
            value=0).grid(row=0, column=0, sticky=tk.W, padx=15, pady=10)
        # radio button widget for web scrape
        web_radio = tk.Radiobutton(
            source_selection, 
            text="Google Web Scrape", 
            font = radio_font,
            variable=self.source,
            background = c3, 
            foreground = "black",
            value=1).grid(row=1, column=0, sticky=tk.W, padx=15, pady=10)
        
        # frame widget to place weather and clothing buttons and outputs
        output_frame = tk.Frame(
            self,
            background=c3)
        output_frame.pack(pady=10)

        # button widget to "generate the weather data"
        generate_weather_info_button = tk.Button(
            output_frame,
            text = "Generate weather data",
            font = button_font,
            command = self.update_weather_output
            ).grid(pady=10, row=0, column=0, padx=15)
        
        # label widget that displays the weather info
        self.weather_info = tk.Label(
            output_frame,
            textvariable = self.weather_output,
            font = long_output_font,
            background=c4,
            foreground="black",
            width=30,
            heigh=12
        ).grid(row=1, column=0, padx=15, pady=10)

        # button widget to "generate an outfit"
        update_clothing_button = tk.Button(
            output_frame,
            text = "Generate Outfit",
            font = button_font,
            command = self.update_clothing_rec
            ).grid(pady=10, row=0, column=1, padx=15)

        # label widget that displays the outfit info 
        self.clothing_info = tk.Label(
            output_frame,
            textvariable = self.clothing_rec,
            font = long_output_font,
            background=c4,
            foreground="black",
            width=30,
            anchor="center",
            height=12,
        ).grid(row=1, column=1, padx=15, pady=10)


        outfits_button = tk.Button(
            self,
            text = "Edit outfits",
            font = button_font,
            command=lambda: controller.show_frame(OutfitsPage),
            width=15
            ).pack(side="right",anchor="sw", padx=15, pady=15)
        
        close_button = tk.Button(
            self,
            text = "Exit",
            font = button_font,
            command=lambda: controller.destroy()
            ).pack(side="left",anchor="se", padx=15, pady=15)
    
    def update_weather_output(self, event=None):
        city = self.city_searched.get()
        
        if not city:
            self.weather_man = None
            self.weather_output.set("Error: Enter a city\nin the box above")
        else:
            try:
                self.weather_man = WeatherMan(city, int(self.source.get()))
                
                self.weather_output.set(self.weather_man.output)
                self.bg_color = "#ffffff"
            except (KeyError, IndexError):
                self.weather_man = None
                self.weather_output.set("Error: Unknown city")
        
    def update_clothing_rec(self):
        try:
            if self.weather_man != None:
                self.outfit_recommender = OutfitRecommender()
                self.outfit_recommender.set_temp(self.weather_man.get_target())
                self.clothing_rec.set(self.outfit_recommender.recommendation) 
            else:
                self.clothing_rec.set("Error: provide weather\ninfo first")
        except ValueError as e:
            print("No outfits provided for that temp")
            self.clothing_rec.set("Error: No outfits provided for that temp")


class OutfitsPage(tk.Frame):
    def __init__(self, parent, controller):

        self.bg_color=c4
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
        self.delete_help = tk.StringVar()
        self.delete_help.set("Tip: use (# from top) as index")

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
            font=title_font
            ).pack(pady=15)
        
        self.outfit_table_frame = tk.Frame(self, width=950)
        self.outfit_table_frame.pack(pady=10, padx=15)

        self.cols = ["Head", "Torso", "Leg", "Foot", "High", "Low"]
        self.tree = ttk.Treeview(
            self.outfit_table_frame, 
            columns=self.cols, 
            show='headings', 
            height=len(self.outfits) if len(self.outfits) < 10 else 10)

        for col in self.cols:
            self.tree.heading(col, text=col, anchor="w")
            self.tree.column(col, width=(944//6), minwidth=150, stretch=False)

        # Set font size
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 18), foreground="black") 
        style.configure("Treeview", font=('Arial', 12), foreground="black") 

        # Configure row styles
        self.tree.tag_configure('oddrow', background=c1)
        self.tree.tag_configure('evenrow', background=c2)
        
        # populate table
        for i, outfit in enumerate(self.outfits):
            tags = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tree.insert("", "end", values=outfit.get_list(), tags=tags)

        self.tree.grid(row=0, column=0)
        
        Add_user_label = tk.Label(
            self,
            background=self.bg_color,
            font=large_lable_font,
            text="Add a new outfit here⬇️"
        ).pack()

        

        # labels and entries for the form to add a new user
        form_bg = c5
        form_frame = tk.Frame(
            self,
            background=form_bg,
            width=950
        )
        form_frame.pack(padx=0, pady=0)

        head_label = tk.Label(
            form_frame,
            text="Head:",
            font=label_font,
            background=form_bg
        ).grid(row=0, column=0, sticky="s")

        head_entry = tk.Entry(
            form_frame,
            font=entry_font,
            textvariable=self.head_entry_text,
            background=c1
        )
        head_entry.grid(row=1, column=0, padx=25, sticky="n")
        head_entry.focus_set()

        torso_label = tk.Label(
            form_frame,
            text="Torso:",
            font=label_font,
            background=form_bg
        ).grid(row=0, column=1, sticky="s")

        torso_entry = tk.Entry(
            form_frame,
            font=entry_font,
            textvariable=self.torso_entry_text,
            background=c1
        ).grid(row=1, column=1, padx=25, sticky="n")

        leg_label = tk.Label(
            form_frame,
            text="Leg:",
            font=label_font,
            background=form_bg,
        ).grid(row=0, column=2, sticky="s")

        leg_entry = tk.Entry(
            form_frame,
            font=entry_font,
            textvariable=self.leg_entry_text,
            background=c1
        ).grid(row=1, column=2, padx=25, sticky="n")
        
        foot_label = tk.Label(
            form_frame,
            text="Foot:",
            font=label_font,
            background=form_bg
        ).grid(row=2, column=0, sticky="s")

        foot_entry = tk.Entry(
            form_frame,
            font=entry_font,
            background=c1,
            textvariable=self.foot_entry_text
        ).grid(row=3, column=0, padx=25, sticky="n")

        high_label = tk.Label(
            form_frame,
            text="High:",
            font=label_font,
            background=form_bg
        ).grid(row=2, column=1, sticky="s")

        high_entry = tk.Entry(
            form_frame,
            font=entry_font,
            background=c1,
            textvariable=self.high_entry_text
        ).grid(row=3, column=1, padx=25, sticky="n")

        low_label = tk.Label(
            form_frame,
            text="Low:",
            font=label_font,
            background=form_bg
        ).grid(row=2, column=2, sticky="s")

        low_entry = tk.Entry(
            form_frame,
            font=entry_font,
            background=c1,
            textvariable=self.low_entry_text
        ).grid(row=3, column=2, padx=25, sticky="n")

        submit_buttom = tk.Button(
            form_frame,
            font= button_font,
            text="Submit",
            command=self.add_outfit_to_csv,
        ).grid(row=5, column=0, padx=10, pady=20)

        error_label = tk.Label(
            form_frame,
            textvariable=self.error_output,
            font=("Arial", 14),
            background=c5
        )
        error_label.grid(row=5, column=1, columnspan=2)

        delete_user_label = tk.Label(
            self,
            background=self.bg_color,
            font=large_lable_font,
            text="Delete Outfit Here⬇️"
        ).pack()
        
        delete_frame = tk.Frame(
            self,
            background=c5,
        )
        delete_frame.pack()

        delete_form_frame = tk.Frame(
            delete_frame,
            background=c5,
            pady=10
        )
        delete_form_frame.grid(row=0, column=0, columnspan=3)

        delete_index_label = tk.Label(
            delete_form_frame,
            background=c5,
            text="Index:",
            font=label_font
        ).grid(row=0, column=0)
    
        delete_index_entry = tk.Entry(
            delete_form_frame,
            font=entry_font,
            textvariable=self.removal_index,
            width=3,
            background=c1,
            fg="black"
        ).grid(row=0, column=1, padx=10)

        submit_buttom = tk.Button(
            delete_form_frame,
            text="Submit",
            font=button_font,
            command=self.remove_outfit_from_csv
        ).grid(row=0, column=2)

        tip_to_delete = tk.Label(
            delete_frame,
            background=c5,
            textvariable=self.delete_help,
            font=label_font,
            width=50
        ).grid(row=2, column=0, columnspan=3, padx=150)

        home_button = tk.Button(
            self,
            text = "Back to home",
            font = button_font,
            command=lambda: controller.show_frame(StartPage),
            width=15
            ).pack(side="right",anchor="se", padx=15, pady=15)
        
        close_button = tk.Button(
            self,
            text = "Exit",
            font = button_font,
            command=lambda: controller.destroy()
            ).pack(side="left",anchor="sw", padx=15, pady=15)

    def remove_outfit_from_csv(self):
        try:
            index = int(self.removal_index.get()) - 1
            self.outfit_recommender.cp.delete_row(index)
            self.repopulate_table()
            self.removal_index.set(value="")
            self.delete_help.set("Outfit removed.")
        except Exception as e:
            self.delete_help.set("Error: Enter Valid # above")
            self.removal_index.set(value="")
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
            self.tree.column(col, width=(944//6), minwidth=150, stretch=False)

        # Additionally, configure the parent frame of the Treeview widget to prevent column resizing:
        self.outfit_table_frame.grid_columnconfigure(0, weight=1)  # Ensure the first (and only) column of the outfit_table_frame widget has a weight of 1

        # Set font size
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 18), foreground="black")  # Adjust the font size here
        style.configure("Treeview", font=('Arial', 12), foreground="black")  # Adjust the font size here

        # Configure row styles
        self.tree.tag_configure('oddrow', background=c1)
        self.tree.tag_configure('evenrow', background=c2)

        # populate table
        for i, outfit in enumerate(self.outfits):
            tags = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tree.insert("", "end", values=outfit.get_list(), tags=tags)

        self.tree.grid(row=0, column=0)
        