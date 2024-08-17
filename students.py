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
    def sidebutton(self, yeargroup):
        global beaviour_vals
        global behaviour_realname
        global aqib
        global aamir
        # Delete widgets
        for widget in self.tabview.tab("Behaviour Report").winfo_children():
            widget.destroy()
        for widget in self.tabview.tab("Spend XP").winfo_children():
            widget.destroy()
        for widget in self.tabview.tab("Award XP").winfo_children():
            widget.destroy()
        

        # Assign names
        with open('behaviour.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        if yeargroup == 13:
            beaviour_vals = data[0]
            behaviour_realname = data[1]
        if yeargroup == 12:
            beaviour_vals = data[2]
            behaviour_realname = data[3]
        if yeargroup == 11:
            beaviour_vals = data[4]
            behaviour_realname = data[5]
        if yeargroup == 10:
            beaviour_vals = data[6]
            behaviour_realname = data[7]
        if yeargroup == 9:
            beaviour_vals = data[8]
            behaviour_realname = data[9]

        with open('xp.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        if yeargroup == 13:
            xp_vals = data[0]
            xp_realname = data[1]
        if yeargroup == 12:
            xp_vals = data[2]
            xp_realname = data[3]
        if yeargroup == 11:
            xp_vals = data[4]
            xp_realname = data[5]
        if yeargroup == 10:
            xp_vals = data[6]
            xp_realname = data[7]
        if yeargroup == 9:
            xp_vals = data[8]
            xp_realname = data[9]

        aqib = "<REDACTED>"

        aamir = "<REDACTED>"

# Functions
        def submit_behaviour():
            print("Submitted")

        def check_points_award():
            global scopes, credentials, file, xp_sheet, indexnumber, inputname, findname, row, col, studentcell, spndingpoints
            scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name("auth_key.json", scopes)
            file = gspread.authorize(credentials)
            xp_sheet = file.open("House Points Tracker Yearly")
            xp_sheet = xp_sheet.worksheet("XP")

        indexnumber = xp_vals.index(self.label_tab_11.get())
        inputname = xp_realname[indexnumber]
        findname = xp_sheet.find(inputname)
        print(inputname)
        print(findname)
        row = findname.row
        col = findname.col
        studentcell = xp_sheet.cell(row, col+2)
        spndingpoints = xp_sheet.cell(row, col+4)
        transaction = xp_sheet.cell(row, col+6)
        self.xp_label1.configure(text=f"{self.label_tab_11.get()} has {studentcell.value} total points and {spndingpoints.value} spending points.")
        if transaction.value == None:
                    self.xp_transaction1.configure(text="No recent awards.")
                    self.xp_transaction1.configure(text=transaction.value)



        def check_points():
            global scopes, credentials, file, xp_sheet, indexnumber, inputname, findname, row, col, studentcell, spndingpoints
            scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name("auth_key.json", scopes)
            file = gspread.authorize(credentials)
            xp_sheet = file.open("House Points Tracker Yearly")
            xp_sheet = xp_sheet.worksheet("XP")

            indexnumber = xp_vals.index(self.label_tab_1.get())
            inputname = xp_realname[indexnumber]
            findname = xp_sheet.find(inputname)
            print(inputname)
            print(findname)
            row = findname.row
            col = findname.col
            col = col + 2
            studentcell = xp_sheet.cell(row, col)
            spndingpoints = xp_sheet.cell(row, col + 2)
            transaction = xp_sheet.cell(row, col + 3)
            self.xp_label.configure(text=f"{self.label_tab_1.get()} has {studentcell.value} total points and {spndingpoints.value} spending points.")
            if transaction.value == None:
                self.xp_transaction.configure(text="No recent transactions.")
            self.xp_transaction.configure(text=transaction.value)

        def submit_points():
            try:
                scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
                credentials = ServiceAccountCredentials.from_json_keyfile_name("auth_key.json", scopes)
                file = gspread.authorize(credentials)
                xp_sheet = file.open("House Points Tracker Yearly")
                xp_sheet = xp_sheet.worksheet("XP")

                indexnumber = xp_vals.index(self.label_tab_1.get())
                inputname = xp_realname[indexnumber]
                findname = xp_sheet.find(inputname)
                print(inputname)
                print(findname)
                row = findname.row
                col = findname.col
                col = col + 2
                col1 = col + 2
                print(col1)
                row1 = row
                print(row1)
                print(row1, col1)
                currentpoints = xp_sheet.cell(row1, col1).value
                print(currentpoints)
                if int(currentpoints) < 0:
                    debt = True
                else:
                    debt = False
            except Exception as e:
                print(e)
            try:
                if debt == False:
                    points = self.reason_xp.get()
                    pspent = xp_sheet.cell(row, col1-1).value
                    newpoints = int(pspent) + int(points)
                    xp_sheet.update_cell(row, col1-1, newpoints)
                    # if the week is in the week beginning of a certain week then add the points to that week
                    today = datetime.now().date()
                    monday = today - timedelta(days=today.weekday())
                    mondaydate = monday.strftime("%d/%m/%Y").replace('/20', '/')
                    oldreason = self.pricetab.get()
                    dayyyte = xp_sheet.find(mondaydate)
                    rowe = dayyyte.row
                    cole = dayyyte.col
                    xp_sheet.update_cell(row, cole, newpoints)

                    reasonappend = xp_sheet.cell(row, col1+1).value
                    timenow = datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y')
                    if reasonappend == None:
                        newreason = f"{timenow} {oldreason}"
                    else:
                        newreason = f"{timenow} {oldreason}\n{reasonappend}"
                    xp_sheet.update_cell(row, col1+1, newreason)
                    self.xp_success()
                elif debt == True:
                    self.xp_failure()
            except Exception as e:
                print(e)

    def submit_points_award():
            try:
                scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
                credentials = ServiceAccountCredentials.from_json_keyfile_name("auth_key.json", scopes)
                file = gspread.authorize(credentials)
                xp_sheet = file.open("House Points Tracker Yearly")
                xp_sheet = xp_sheet.worksheet("XP")
                indexnumber = xp_vals.index(self.label_tab_11.get())
                inputname = xp_realname[indexnumber]
                findname = xp_sheet.find(inputname)
                print(inputname)
                print(findname)
                row = findname.row
                col = findname.col
                pointscol = col + 2
                currentpoints = xp_sheet.cell(row, pointscol).value
                print(currentpoints)
                if int(currentpoints) < 0:
                    debt = True
                else:
                    debt = False
            except Exception as e:
                print(e)
            try:
                if debt == False:
                    points = self.reason_xp1.get()
                    newpoints = int(currentpoints) + int(points)
                    xp_sheet.update_cell(row, pointscol, newpoints)
                    oldreason = self.pricetab1.get()
                    today = datetime.now().date()
                    monday = today - timedelta(days=today.weekday())
                    print("here")
                    mondaydate = monday.strftime("%d/%m/%Y").replace('/20', '/')
                    oldreason = self.pricetab1.get()
                    dayyyte = xp_sheet.find(mondaydate)
                    cole = dayyyte.col
                    xp_sheet.update_cell(row, cole, newpoints)
                    reasonappend = xp_sheet.cell(row, pointscol+4).value
                    print("here again")
                    timenow = datetime.strftime(datetime.now(), '%d/%m/%Y')
                    print("nothere")
                    if reasonappend == None:
                        newreason = f"{timenow} {oldreason}"
                    else:
                        newreason = f"{timenow} {oldreason}\n{reasonappend}"
                    xp_sheet.update_cell(row, pointscol+4, newreason)
                    self.xp_success1()
                elif debt == True:
                    print("Failed")
                    self.xp_failure
            except Exception as e:
                print(e)

    # Behaviour Stuff
        self.bigtitle = customtkinter.CTkLabel(self.tabview.tab("Behaviour Report"), text="Behaviour Report", width=500, height=40, font=customtkinter.CTkFont(size=40, weight="bold"))
        self.bigtitle.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.label_tab_1_behav = customtkinter.CTkOptionMenu(self.tabview.tab("Behaviour Report"), values=beaviour_vals, width=500, height=40)
        self.label_tab_1_behav.grid(row=1, column=0, padx=20, pady=20)

        self.reason = customtkinter.CTkEntry(self.tabview.tab("Behaviour Report"), placeholder_text="Reason", width=500, height=40)
        self.reason.grid(row=3, column=0, padx=20, pady=20)

        self.multiradiobox = customtkinter.CTkOptionMenu(self.tabview.tab("Behaviour Report"), values=["Homework", "Late", "Behaviour"], width=500, height=40)
        self.multiradiobox.grid(row=2, column=0, padx=20, pady=20)

        self.issuedby = customtkinter.CTkEntry(self.tabview.tab("Behaviour Report"), placeholder_text="Issued By", width=500, height=40)
        self.issuedby.grid(row=4, column=0, padx=20, pady=20)
        
        self.detentionlabel = customtkinter.CTkLabel(self.tabview.tab("Behaviour Report"), text="", width=500, height=40, font=customtkinter.CTkFont(size=20))
        self.detentionlabel.grid(row=5, column=0, padx=20, pady=20)


        self.amount_of_detentions = customtkinter.CTkButton(self.tabview.tab("Behaviour Report"), text="Amount of detentions", command=self.detention_number, width=500, height=40)
        self.amount_of_detentions.grid(row=6, column=0, padx=20, pady=20)

        self.submit = customtkinter.CTkButton(self.tabview.tab("Behaviour Report"), text="Submit", command=self.submit_behaviour, width=500, height=40)
        self.submit.grid(row=7, column=0, padx=20, pady=20)


                
