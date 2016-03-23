# Copyright (c) 2011 Cuong Ngo
# GUI Fishing Game

import random
from tkinter import *
import shelve
from sys import exit
import shelve
users = shelve.open("fishing")
random.seed()
fisher = None
class Fishing(Frame):
    "GUI fishing game"

    def __init__(self):
        random.seed()
        # Set up the GUI framework
        root = Tk()
        root.title('G-Fish')
        super(Fishing, self).__init__(root)
        self.grid()
        # Create the widgets
        w_fishG = Button(self, text = "Fish As", command = self.fisher)
        w_fishG.grid(row = 0, column = 0)
        self.w_textG = Entry(self)
        self.w_textG.grid(row = 0, column = 1)
        w_registerG = Button(self, text = "Register", command = self.register)
        w_registerG.grid(row = 0, column = 2)
        w_castG = Button(self, text = "Cast", command = self.cast)
        w_castG.grid(row = 1, column = 0)
        self.feedbackG = Label(self)
        self.feedbackG.grid(row = 1, column = 1)
        self.scoreG = Label(self)
        self.scoreG.grid(row = 1, column = 2)
        root.mainloop()
    def register(self):
        username = self.w_textG.get()
        for c in username:
            if not c.isalpha() and not c.isdigit() and not c in "_-":
                self.feedbackG.configure(text = "illegal character in username")
                return
        if username in users:
            self.feedbackG.configure(text = "username already registered")
            return
        else:
            self.feedbackG.configure(text = "welcome new fisher")
        users[username] = 0
        users.sync()
    def fisher(self):
        username = self.w_textG.get()
        global fisher
        if not (username in users):
            self.feedbackG.configure(text = "username unknown")
            return
        fisher = username
    def cast(self):
        global fisher
        if fisher == None:
            self.feedbackG.configure(text = "Click fish button to choose a fisher.")
            return
        fishes = int(random.randint(1, 100))
        if fishes < 21:
            users[fisher] += 0
            self.feedbackG.configure(text = "You caught Nothing!")
        elif 20 < fishes < 41:
            users[fisher] += 10
            self.feedbackG.configure(text = "You have caught a Minnow!")
        elif 40 < fishes < 71:
            users[fisher] += 30
            self.feedbackG.configure(text = "You have caught a Bluegill!")                                   
        elif 70 < fishes < 86:
            users[fisher] += 100
            self.feedbackG.configure(text = "You have caught a Bass!")
        elif 85 < fishes < 96:
            users[fisher] += 200
            self.feedbackG.configure(text = "You have caught a Trout!")
        elif 95 < fishes < 99:
            users[fisher] += 500
            self.feedbackG.configure(text = "You have caught a Salmon!")
        elif fishes == 100:
            users[fisher] += 5000
            self.feedbackG.configure(text = "You have caught a Gold Boot!")
        self.scoreG.configure(text = str(users[fisher]))
_ = Fishing()
