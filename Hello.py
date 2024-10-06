#from tkinter import *
import tkinter as tk
from tkinter import messagebox
class Form1(tk.Frame):
    """ Create form """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createwidgets()

    def createwidgets(self):
        """ Create form """
        tk.Label(self, text="Name:", width=20).grid(row=0, column=0)
        self.txtname = tk.StringVar() 
        tk.Entry(self, width=50, textvariable=self.txtname).grid(row=0, column=1)

        tk.Label(self, text="Contact:", width=20).grid(row=1, column=0)
        self.txtcontact = tk.StringVar()
        tk.Entry(self, width=50, textvariable=self.txtcontact).grid(row=1, column=1)

        #tk.Label(self, text="Address:", width=20).grid(row=2, column=0)
        #self.txtaddress = tk.Text(self, height=5, width=50).grid(row=2, column=1)

        self.submitbtn = tk.Button(text="Submit", height=1, width=20, command=self.validate)
        self.submitbtn.grid(row=3, column=0)

    def validate(self):
        """ Called when button is clicked"""  
        
        if self.txtname.get() == "" or self.txtcontact.get() == "":
          messagebox.showinfo("Validation", "Please enter all the details")
        else:
          messagebox.showinfo("Details:", "Details Saved")   
    

ROOT = tk.Tk()
#modify root window
ROOT.title("Sample Window")
ROOT.geometry("500x500")

APP = Form1(ROOT)

ROOT.mainloop()
