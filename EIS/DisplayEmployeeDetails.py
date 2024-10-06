from tkinter import *
import pypyodbc
import AddEmployee

class EmployeeDetails(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)                         
        
        self.DisplayEmpDetails()             
        
    def DisplayEmpDetails(self):
        
        AddEmployee.DisplayEmpDetails(self)
        

    

 

   