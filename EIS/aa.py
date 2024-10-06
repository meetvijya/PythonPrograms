from tkinter import *
from tkinter import messagebox

class Tela_login(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.grid()
        self.button1 = Button(text = "Open",command = lambda:self.open_login())
        self.button1.grid()

    def open_login(self):
        root2 = Toplevel()
        app2 = Tela_principal(root2)

class Tela_principal(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.grid
        messagebox.showinfo("Login", "Invalid User crendential")
        
root = Tk()
root.geometry("800x600")
app = Tela_login(root)
root.mainloop()
