from tkinter import *
from tkinter import messagebox
import pypyodbc
from DisplayEmployeeDetails  import *

#conn
#cur = conn.cursor

def ConnectDatabase():
    global cur
    global conn
    pypyodbc.lowercase = False        
    conn = pypyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb)};" +
    r"Dbq=C:\Temp\Python Project\EIS\EmployeeDB.mdb;")
    cur = conn.cursor()

def DisconnectDatabase():
    global cur
    global conn
    cur.close()
    conn.close()      

class Employee(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #self.label1 = Label(Tops,text="Employee Information" ,fg="black",font = ("arial",10,"bold")).grid(row=0,column=0,columnspan=2 )
        Tops = LabelFrame(master,text="Add Employee",height=200,font = ("arial",10,"bold"),bd=8)
        Tops.pack(side="top",fill="x")

        self.BottomFrame = LabelFrame(master,text="Employee details",font = ("arial",10,"bold"),bd=8)
        self.BottomFrame.pack(side="top" ,fill="x")
        
        
       
        self.lblempname = Label(Tops,text="Employee Name:",fg="black").grid(row=1,column=0)
        self.txtempname = Entry(Tops)
        self.txtempname.grid(row=1,column=1)
        self.txtempname.focus()

        self.lblempcontact = Label(Tops,text="Employee Contact:",fg="black").grid(row=2,column=0)
        self.txtempcontact = Entry(Tops)
        self.txtempcontact.grid(row=2,column=1)

        self.lblempAddress = Label(Tops,text="Employee Address:",fg="black").grid(row=3,column=0)
        self.txtempaddress = Text(Tops, height=5,width=15)
        self.txtempaddress.grid(row=3,column=1)

        self.btnSubmit = Button(Tops,text="Submit",fg="black", command=lambda:self.InsertEmpDetails()).grid(row=4,column=0 )
        
        DisplayEmpDetails(self.BottomFrame)
        
   
    def InsertEmpDetails(self):
        name = self.txtempname.get()
        contact = int(self.txtempcontact.get())
        address = self.txtempaddress.get(1.0,END)[:-1] # Removes \n added automatically at the end of text box data
        args = (name,contact,address)
        query = "Insert into Employee(empname,empcontact,empaddress) " \
                "values('%s','%d','%s')" %(args)
        
        ConnectDatabase()
        cur.execute(query)
         
        conn.commit()
        messagebox.showinfo("emp details","Details Saved")

        self.txtempname.delete(0, END)
        self.txtempcontact.delete(0, END)
        self.txtempaddress.delete('1.0', END)
        DisconnectDatabase()
        #Reload Employee details
        DisplayEmpDetails(self.BottomFrame)
    

def DisplayEmpDetails(parent):
    rows =[]
    cols1 = []
    colnames = ("Emp Id","Emp Name","Emp Contact", "Address")
    for k in range(4):
        e = Entry(parent,relief=RIDGE) 
        e.grid(row=0, column=k, sticky=NSEW)
        e.insert(END, colnames[k])
        cols1.append(e)
    rows.append(cols1)    
    ConnectDatabase()
    cur.execute("SELECT ID, empname, empcontact, empaddress FROM Employee")
    r = 1
    while True:
        row= cur.fetchone()
        if row is None:
            break
        cols = []
        for j in range(4):
            e = Entry(parent,relief=RIDGE) 
            e.grid(row=r, column=j, sticky=NSEW)
            e.insert(END, row[j])
            cols.append(e)
        r = r + 1    
        rows.append(cols)
    #messagebox.showinfo("Employee Detail",u"ID: {0} Name:{1} Contact:{2} Address:{3}".format(
        #row.get("ID"), row.get("empname"), row.get("empcontact"), row.get("empaddress")))

    DisconnectDatabase() 
        

