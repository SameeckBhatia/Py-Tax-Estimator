import tkinter as tk
from calculator import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(2)

win = tk.Tk()
win.geometry("400x600")
win.config(background="#2D3339")
win.resizable(width=False, height=False)
win.title("Tax Estimator")

# Labels
label1 = tk.Label(win, text="Select country", font=("Segoe UI", 14),
                  background="#2D3339", foreground="#FBF4E9")
label1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

label2 = tk.Label(win, text="Select state/province", font=("Segoe UI", 14),
                  background="#2D3339", foreground="#FBF4E9")
label2.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

# Dropdowns
options = ["Canada", "United States"]
choice1 = tk.StringVar(win)
choice1.set("(country)")
dropdown1 = tk.OptionMenu(win, choice1, *options)
dropdown1.place(relx=0.5, rely=0.2, relwidth=0.5, anchor=tk.CENTER)

choice2 = tk.StringVar(win)
choice2.set("(state/province)")
dropdown2 = tk.OptionMenu(win, choice2, "")
dropdown2.place(relx=0.5, rely=0.45, relwidth=0.5, anchor=tk.CENTER)

win.mainloop()
