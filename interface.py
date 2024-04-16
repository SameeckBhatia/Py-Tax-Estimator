import tkinter as tk
from calculator import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(2)

win = tk.Tk()
win.geometry("400x600")
win.config(background="#2D3339")
win.resizable(width=False, height=False)
win.title("Tax Estimator")

country_state_dict = {"Canada": ["British Columbia", "Ontario"],
                      "United States": ["California", "Florida", "Pennsylvania",
                                        "New York", "Texas"]}


def update_options(*args):
    dropdown2["menu"].delete(0, "end")

    selected_value = choice1.get()

    second_options = country_state_dict[selected_value]

    for option in second_options:
        dropdown2["menu"].add_command(label=option,
                                      command=tk._setit(choice2, option))


# Labels
label1 = tk.Label(win, text="Select country", font=("Segoe UI", 14),
                  background="#2D3339", foreground="#FBF4E9")
label1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

label2 = tk.Label(win, text="Select state/province", font=("Segoe UI", 14),
                  background="#2D3339", foreground="#FBF4E9")
label2.place(relx=0.5, rely=0.32, anchor=tk.CENTER)

label3 = tk.Label(win, text="Enter income", font=("Segoe UI", 14),
                  background="#2D3339", foreground="#FBF4E9")
label3.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# Dropdowns
options = ["Canada", "United States"]
choice1 = tk.StringVar(win)
choice1.set("(country)")
dropdown1 = tk.OptionMenu(win, choice1, *options)
dropdown1.place(relx=0.5, rely=0.2, relwidth=0.5, anchor=tk.CENTER)

choice2 = tk.StringVar(win)
choice2.set("(state/province)")
dropdown2 = tk.OptionMenu(win, choice2, "")
dropdown2.place(relx=0.5, rely=0.42, relwidth=0.5, anchor=tk.CENTER)

choice1.trace("w", update_options)

# Entries
entry1 = tk.Entry(win, font=("Segoe UI", 12), background="#434C56",
                  foreground="#FBF4E9")
entry1.place(relx=0.5, rely=0.65, relwidth=0.5, anchor=tk.CENTER)


# Button function
def display_tax():
    country, state, income = choice1.get(), choice2.get(), float(entry1.get())
    total_tax = (Federal(country, income).total_tax() +
                 State(country, state, income).total_tax())
    avg_rate = 100 * (total_tax / income)
    net_income = income - total_tax

    win1 = tk.Tk()
    win1.geometry("600x300")
    win1.config(background="#2D3339")
    win1.resizable(width=False, height=False)
    win1.title("Estimate")

    tk.Label(win1, text=f"You owe ${total_tax:,.2f} in total taxes",
             font=("Segoe UI", 14), background="#2D3339",
             foreground="#FBF4E9").place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    tk.Label(win1, text=f"The average rate is {avg_rate:.2f}%",
             font=("Segoe UI", 14), background="#2D3339",
             foreground="#FBF4E9").place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    tk.Label(win1, text=f"Your net income is ${net_income:,.2f}%",
             font=("Segoe UI", 14), background="#2D3339",
             foreground="#FBF4E9").place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    win1.mainloop()


# Buttons
button1 = tk.Button(win, text="Calculate", command=display_tax,
                    font=("Segoe UI", 11), foreground="#FBF4E9",
                    background="#E65A45")
button1.place(relx=0.5, rely=0.85, anchor=tk.CENTER, relwidth=0.4,
              relheight=0.1)

win.mainloop()
