import tkinter as tk
from calculator import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(2)

win = tk.Tk()
win.geometry("400x600")
win.config(background="#2D3339")
win.resizable(width=False, height=False)
win.title("Tax Estimator")

win.mainloop()
