import tkinter 
from tkinter import messagebox
from AddEmployee import *
import os
import csv

class MainMenu(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.root = parent
        # create menu bar
        self.menubar = Menu(parent)

        # create sub menu
        self.filemenu = Menu(self.menubar, tearoff=0)

        # Add command to sub menu
        self.filemenu.add_command(label="Add Employee", command=lambda:self.ShowAddEmployeeWindow())
        self.filemenu.add_command(label="Show Employee details", command=lambda:self.DisplayEmpDetails())
        self.filemenu.add_command(label="Read CSV",command=lambda:self.ReadWriteCSV())
        self.filemenu.add_command(label="Write CSV",command=lambda:self.WriteCSV())
        self.filemenu.add_command(label="Exit",command= parent.destroy)
        
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        parent.config(menu=self.menubar)

    def ShowAddEmployeeWindow(self):
        addempwindow = Toplevel()
        addempApp = Employee(addempwindow)
        
        
        addempwindow.title("Add Employee")
        addempwindow.geometry("1280x800+0+50")        
        addempwindow.focus_force()
        addempwindow.mainloop()

    def DisplayEmpDetails(self):
        
        empDetailsWindow = Toplevel()
        empDetailsWindow.title("Employee Details")
        empDetailsWindow.geometry("800x600")

        detailsapp = EmployeeDetails(empDetailsWindow)
        detailsapp.pack()#(side="top",fill="x")
        empDetailsWindow.mainloop()    

    def file_is_empty(self,filename):
        return os.stat(filename).st_size==0
    
    def ReadWriteCSV(self):
        filename = r"C:\Temp\EggPlant Training\C2ImportCalEventSample.csv"
        #filename = r"C:\Temp\EggPlant Training\PatientInformation.csv"

        #reading csv file
        
        with open(filename,'r') as csvfile:
            #create reader object
            csvreader = csv.reader(csvfile)
            #extracting field name
            if not self.file_is_empty(filename):               
                # r and c tell us where to grid the labels
                r = 0
                for col in csvreader:
                    c = 0
                    for row in col:
                        # i've added some styling
                        label = tkinter.Label(self.root, width = 10, height = 2, \
                                            text = row, relief = tkinter.RIDGE)                        
                        label.grid(row = r, column = c)                        
                        c += 1
                    r += 1                  
                csvfile.close()
            else:
                messagebox.showinfo("Master","File is empty")


    def WriteCSV(self):            
        filename = r"C:\Temp\EggPlant Training\C2ImportCalEventSample.csv"
        #filename = r"C:\Temp\EggPlant Training\PatientInformation.csv"
        rowdata = ["9/5/2018",	"9:00:00 PM",	"9/5/2018",	"7:00:00 PM",	"Scrum Meeting",	"N",	"N",\
        	"Curriculum Meeting",	"Vijay Sawant",	"meetvijya@domain.com",	"814-555-5179",	\
            "KV High School",	"2",	"N",	"N",	"25",	"9/2/2018s"]
        with open(filename,"a") as csvfile:
            csvwriter = csv.writer(csvfile)           
            csvwriter.writerow(rowdata)

