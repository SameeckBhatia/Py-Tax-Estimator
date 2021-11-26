#Importing libraries
from ctypes import windll; from tkinter import *

#Importing functions from respective files
from ausCode import australia; from britCode import uk;
from canCode import canada; from amCode import states

windll.shcore.SetProcessDpiAwareness(1)

#Creating window and setting size
win=Tk()
win.geometry("550x350")

#Defining tax function
def tax():
    if a.get().lower() == "australia":
        australia(a, b, owed, perc)
    elif a.get().lower() == "canada":
        canada(a, b, owed, perc)
    elif a.get().lower() == "uk":
        uk(a, b, owed, perc)
    elif a.get().lower() == "us" or a.get().lower() == "usa":
        states(a, b, owed, perc)
    else:
        owed.config(text = "Invalid input")
        perc.config(text = "null%")

#Collecting input to calculate based on country
Label(win, text="Enter country: ", font = "Bahnschrift 11").place(x = "50", y = "40")
a = Entry(win, width=20)
a.place(x = "50", y = "80")

#Collecting income to calculate tax owed
Label(win, text="Enter income: ", font = "Bahnschrift 11").place(x = "50", y = "140")
b = Entry(win, width=20)
b.place(x = "50", y = "180")

Button(win, text="Calculate", font = "Bahnschrift 11", height = "1", width = "15", comman = tax).place(x = "50", y = "255")
Button(win, text="End program", font = "Bahnschrift 11", height = "1", width = "15", command = win.quit).place(x = "300", y = "255")

owed = Label(win, text="<tax owed>", font = "Bahnschrift 11")
owed.place(x = "330", y = "65")

perc = Label(win, text="<tax percent>", font = "Bahnschrift 11")
perc.place(x = "325", y = "165")

win.mainloop()