# importing libraries
from ctypes import windll
from tkinter import *

windll.shcore.SetProcessDpiAwareness(1)

# creating window and setting size
win = Tk()
win.geometry("610x350")


# defining tax function
def tax():
    if variable.get() == "Australia":

        australia(b, owed, perc, net)

    elif variable.get() == "Canada":

        canada(b, owed, perc, net)

    elif variable.get() == "UK":

        uk(b, owed, perc, net)

    elif variable.get() == "USA":

        states(b, owed, perc, net)

    else:

        owed.config(text="null", font="Courier 11 bold")
        net.config(text="null", font="Courier 11 bold")
        perc.config(text="null", font="Courier 11 bold")


# defining australia function
def australia(country_input, tax_owed, tax_percent, net_income):
    # lists with Australian brackets
    federal_brackets = [0, 18200, 45000, 120000, 180000]
    federal_rates = [0, 0, 0.19, 0.325, 0.37, 0.45]

    # initial user input
    income = float(country_input.get())

    # if statement to make sure input is greater than 0
    if income >= 0:

        tax_value = 0
        percent = 0.0
        sum_below = [0]

        # appending list sum_below with the sum of tax owed in lower brackets
        for j in range(1, len(federal_brackets)):
            s = round((federal_brackets[j] - federal_brackets[j - 1]) * federal_rates[j] + sum_below[j - 1])

            sum_below.append(s)

        # loop to calculate tax and percent owed
        for i in range(len(federal_brackets) - 1):

            # statements to find the correct bracket interval
            if income in range(federal_brackets[1]):

                tax_value = federal_rates[1] * income
                percent = (tax_value / income) * 100

            elif income in range(federal_brackets[i], federal_brackets[i + 1]):

                tax_value = (income - federal_brackets[i]) * federal_rates[i + 1] + sum_below[i]
                percent = (tax_value / income) * 100

            elif income >= federal_brackets[-1]:

                tax_value = (income - federal_brackets[-1]) * federal_rates[-1] + sum_below[-1]
                percent = (tax_value / income) * 100

        # output values to user
        tax_owed.config(text="A$" + str(round(tax_value, 1)))
        net_income.config(text="A$" + str(round(income - tax_value, 1)))
        tax_percent.config(text=str(round(percent, 1)) + "%")

    else:

        tax_owed.config(text="Invalid input")
        tax_percent.config(text="null")


# defining canada function
def canada(country_input, tax_owed, tax_percent, net_income):
    # lists with Canadian brackets and standard deduction
    federal_brackets = [0, 50197, 100392, 155625, 221708]
    federal_rates = [0, 0.15, 0.205, 0.26, 0.29, 0.33]
    sd = 14398

    # initial user input
    income = float(country_input.get()) - sd

    # if statement to make sure input is greater than 0
    if income >= -sd:

        tax_value = 0
        percent = 0.0
        sum_below = [0]

        # appending list sum_below with the sum of tax owed in lower brackets
        for j in range(1, len(federal_brackets)):
            s = round((federal_brackets[j] - federal_brackets[j - 1]) * federal_rates[j] + sum_below[j - 1])

            sum_below.append(s)

        # loop to calculate tax and percent owed
        for i in range(len(federal_brackets) - 1):

            # statements to find the correct bracket interval
            if income in range(federal_brackets[1]):

                tax_value = federal_rates[1] * income
                percent = (tax_value / (income + sd)) * 100

            elif income in range(federal_brackets[i], federal_brackets[i + 1]):

                tax_value = (income - federal_brackets[i]) * federal_rates[i + 1] + sum_below[i]
                percent = (tax_value / (income + sd)) * 100

            elif income >= federal_brackets[-1]:

                tax_value = (income - federal_brackets[-1]) * federal_rates[-1] + sum_below[-1]
                percent = (tax_value / (income + sd)) * 100

        # output values to user
        tax_owed.config(text="C$" + str(round(tax_value, 1)))
        net_income.config(text="C$" + str(round(income + sd - tax_value, 1)))
        tax_percent.config(text=str(round(percent, 1)) + "%")

    else:

        tax_owed.config(text="Invalid input")
        tax_percent.config(text="null")


# defining uk function
def uk(country_input, tax_owed, tax_percent, net_income):
    # lists with British brackets
    federal_brackets = [0, 12570, 50270, 150000]
    federal_rates = [0, 0, 0.20, 0.40, 0.45]

    # initial user input
    income = float(country_input.get())

    # if statement to make sure input is greater than 0
    if income >= 0:

        tax_value = 0
        percent = 0.0
        sum_below = [0]

        # appending list sum_below with the sum of tax owed in lower brackets
        for j in range(1, len(federal_brackets)):
            s = round((federal_brackets[j] - federal_brackets[j - 1]) * federal_rates[j] + sum_below[j - 1])

            sum_below.append(s)

        # loop to calculate tax and percent owed
        for i in range(len(federal_brackets) - 1):

            # statements to find the correct bracket interval
            if income in range(federal_brackets[1]):

                tax_value = federal_rates[1] * income
                percent = (tax_value / income) * 100

            elif income in range(federal_brackets[i], federal_brackets[i + 1]):

                tax_value = (income - federal_brackets[i]) * federal_rates[i + 1] + sum_below[i]
                percent = (tax_value / income) * 100

            elif income >= federal_brackets[-1]:

                tax_value = (income - federal_brackets[-1]) * federal_rates[-1] + sum_below[-1]
                percent = (tax_value / income) * 100

        # output values to user
        tax_owed.config(text="£" + str(round(tax_value, 1)))
        net_income.config(text="£" + str(round(income - tax_value, 1)))
        tax_percent.config(text=str(round(percent, 1)) + "%")

    else:

        tax_owed.config(text="Invalid input")
        tax_percent.config(text="null")


# defining states function
def states(country_input, tax_owed, tax_percent, net_income):
    # lists with American brackets and standard deduction
    federal_brackets = [0, 10275, 41775, 89075, 170050, 215950, 539900]
    federal_rates = [0, 0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    sd = 12950

    # initial user input
    income = float(country_input.get()) - sd

    # if statement to make sure input is greater than 0
    if income >= -sd:

        tax_value = 0
        percent = 0.0
        sum_below = [0]

        # appending list sum_below with the sum of tax owed in lower brackets
        for j in range(1, len(federal_brackets)):
            s = round((federal_brackets[j] - federal_brackets[j - 1]) * federal_rates[j] + sum_below[j - 1])

            sum_below.append(s)

        # loop to calculate tax and percent owed
        for i in range(len(federal_brackets) - 1):

            # statements to find the correct bracket interval
            if income in range(federal_brackets[1]):

                tax_value = federal_rates[1] * income
                percent = (tax_value / (income + sd)) * 100

            elif income in range(federal_brackets[i], federal_brackets[i + 1]):

                tax_value = (income - federal_brackets[i]) * federal_rates[i + 1] + sum_below[i]
                percent = (tax_value / (income + sd)) * 100

            elif income >= federal_brackets[-1]:

                tax_value = (income - federal_brackets[-1]) * federal_rates[-1] + sum_below[-1]
                percent = (tax_value / (income + sd)) * 100

        # income limit for FICA tax
        if income > 147000:

            tax_value += 9114 + (0.0145 * (income + sd))
            percent = (tax_value / income) * 100

        else:

            tax_value += 0.0765 * (income + sd)
            percent += 7.65

        # output values to user
        tax_owed.config(text="$" + str(round(tax_value, 1)))
        net_income.config(text="$" + str(round(income + sd - tax_value, 1)))
        tax_percent.config(text=str(round(percent, 1)) + "%")

    else:

        owed.config(text="Invalid input")
        perc.config(text="null")


# collecting input from dropdown
choices = ["Australia", "Canada", "UK", "USA"]
variable = StringVar()
variable.set('-----')

Label(win, text="Select country: ", font="Bahnschrift 11").place(x="50", y="40")
a = OptionMenu(win, variable, *choices)
a.config(width="13", font="Bahnschrift 10")
a.place(x="50", y="80")

# collecting income to calculate tax owed
Label(win, text="Enter annual income: ", font="Bahnschrift 11").place(x="50", y="140")
b = Entry(win, width=20)
b.place(x="50", y="180")

# buttons and labels
Button(win, text="Calculate", font="Bahnschrift 11", width="15", command=tax).place(x="175", y="255")

Label(win, text="Tax owed:", font="Bahnschrift 11").place(x="300", y="50")
owed = Label(win, font="Bahnschrift 11")
owed.place(x="450", y="50")

Label(win, text="Net income:", font="Bahnschrift 11").place(x="300", y="115")
net = Label(win, font="Bahnschrift 11")
net.place(x="450", y="115")

Label(win, text="Tax percent:", font="Bahnschrift 11").place(x="300", y="180")
perc = Label(win, font="Bahnschrift 11")
perc.place(x="450", y="180")

win.mainloop()
