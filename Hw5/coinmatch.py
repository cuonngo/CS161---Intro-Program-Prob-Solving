# Copyright (c) 2011 Cuong Ngo 

from tkinter import*
import random

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.yourscore = 0
        self.myscore = 0
        self.create_widgets()
        
    def create_widgets(self):
        # create description label
        Label(self,
              text = "You"
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,
              text = "Your Score"
              ).grid(row = 3, column = 0, sticky = W)
        Label(self,
              text = "My Score"
              ).grid(row = 3, column = 1, sticky = W)

        # create score
        self.lbl = Label(self)
        self.lbl["text"] = self.myscore
        self.lbl.grid(row = 4, column = 0)

        self.lbl2 = Label(self)
        self.lbl2["text"] = self.yourscore
        self.lbl2.grid(row = 4, column = 1)

        # create button
        Button(self,
               text = "Heads",
               command = self.flipcoin
               ).grid(row = 1, column = 0, sticky = W)
        Button(self,
               text = "Tails",
               command = self.flipcoin
               ).grid(row = 1, column = 1, sticky = W)

    def flipcoin(self):
        flip = random.choice(["Head", "Tail"])
        if flip == "Head":
            self.yourscore += 1
            self.lbl["text"] = self.yourscore
        else:
            self.myscore += 1
            self.lbl2["text"] = self.myscore


root = Tk()
root.title("Coin Match")
app = Application(root)
root.mainloop()
        
