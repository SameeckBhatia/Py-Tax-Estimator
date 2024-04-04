import tkinter as tk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(2)

win = tk.Tk()
win.geometry("500x400")

win.title("Tax Estimator")

win.mainloop()
