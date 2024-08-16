import tkinter
import tkinter.messagebox
import customtkinter
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import time
import smtplib
import requests
from datetime import datetime, timedelta

customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("loxford school")
        self.geometry(f"{1300}x{870}")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Loxford School", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.year11sidebutton, text="Year 13")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.year10sidebutton, text="Year 12")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.year9sidebutton, text="Year 11")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.year8sidebutton, text="Year 10")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.year7sidebutton, text="Year 9")
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)

        new_scaling = "120%"
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=900, height=600)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Behaviour Report")
        self.tabview.add("Spend XP")
        self.tabview.add("Award XP")
        self.tabview.tab("Behaviour Report").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Spend XP").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Award XP").grid_columnconfigure(0, weight=1)

        self.names = customtkinter.CTkLabel(self.tabview.tab("Behaviour Report"), text="Welcome to the Behaviour System!", width=500, height=40, font=customtkinter.CTkFont(size=35, weight="bold"))
        self.names.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.names1 = customtkinter.CTkLabel(self.tabview.tab("Behaviour Report"), text="Click on a year group on the side to get started.", font=customtkinter.CTkFont(size=20), width=500, height=40)
        self.names1.grid(row=2, column=0, padx=20, pady=(20, 10))
        # ygs.trace("w", yeargroup)

        self.names11 = customtkinter.CTkLabel(self.tabview.tab("Spend XP"), text="Welcome to the XP Spending Tab!", width=500, height=40, font=customtkinter.CTkFont(size=35, weight="bold"))
        self.names11.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.names111 = customtkinter.CTkLabel(self.tabview.tab("Spend XP"), text="Click on a year group on the side to get started.", font=customtkinter.CTkFont(size=20), width=500, height=40)
        self.names111.grid(row=2, column=0, padx=20, pady=(20, 10))

        self.names112 = customtkinter.CTkLabel(self.tabview.tab("Award XP"), text="Welcome to the XP Awarding Tab!", width=500, height=40, font=customtkinter.CTkFont(size=35, weight="bold"))
        self.names112.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.names1112 = customtkinter.CTkLabel(self.tabview.tab("Award XP"), text="Click on a year group on the side to get started.", font=customtkinter.CTkFont(size=20), width=500, height=40)
        self.names1112.grid(row=2, column=0, padx=20, pady=(20, 10))


        # set default values
    
    def updatlol(self):
        pass
