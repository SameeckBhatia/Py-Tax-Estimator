#Importing libraries
from ctypes import windll; from tkinter import *

#Importing functions from respective files
from ausCode import australia; from britCode import uk;
from canCode import canada; from amCode import states

windll.shcore.SetProcessDpiAwareness(1)

#Creating window and setting size
win = Tk()
win.geometry("610x350")

#Defining tax function
def tax():
    if variable.get() == "Australia" and b.get() is int:
        australia(a, b, owed, perc, net)
    elif variable.get() == "Canada" and b.get() is int:
        canada(a, b, owed, perc, net)
    elif variable.get() == "UK" and b.get() is int:
        uk(a, b, owed, perc, net)
    elif variable.get() == "USA" and b.get() is int:
        states(a, b, owed, perc, net)
    else:
        owed.config(text = "null", font = "Courier 11 bold")
        net.config(text = "null", font = "Courier 11 bold")
        perc.config(text = "null", font = "Courier 11 bold")

#Collecting input from dropdown
choices = ["Australia", "Canada", "UK", "USA"]
variable = StringVar()
variable.set('-----')

Label(win, text = "Select country: ", font = "Bahnschrift 11").place(x = "50", y = "40")
a = OptionMenu(win, variable, *choices)
a.config(width = "13", font = "Bahnschrift 9")
a.place(x = "50", y = "80")

#Collecting income to calculate tax owed
Label(win, text = "Enter income: ", font = "Bahnschrift 11").place(x = "50", y = "140")
b = Entry(win, width = 20)
b.place(x = "50", y = "180")

#Buttons and labels
Button(win, text = "Calculate", font = "Bahnschrift 11", height = "1", width = "15", command = tax).place(x = "50", y = "255")
Button(win, text = "End program", font = "Bahnschrift 11", height = "1", width = "15", command = win.quit).place(x = "300", y = "255")

Label(win, text = "Tax owed:", font = "Bahnschrift 11").place(x = "300", y = "50")
owed = Label(win, font = "Bahnschrift 11")
owed.place(x = "450", y = "50")

Label(win, text = "Net income:", font = "Bahnschrift 11").place(x = "300", y = "115")
net = Label(win, font = "Bahnschrift 11")
net.place(x = "450", y = "115")

Label(win, text = "Tax percent:", font = "Bahnschrift 11").place(x = "300", y = "180")
perc = Label(win, font = "Bahnschrift 11")
perc.place(x = "450", y = "180")

win.mainloop()