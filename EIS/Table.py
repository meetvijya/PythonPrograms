from tkinter import *

rows = []
for i in range(7):
    cols = []
    for j in range(4):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)

def onPress():
    for row in rows:
        for col in row:
            print(col.get())
        

Button(text='Fetch', command=onPress).grid()
mainloop()
