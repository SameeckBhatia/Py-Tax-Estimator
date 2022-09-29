def states(a, b, owed, perc, net):
    ustx = [0, 0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    usbrk = [0, 10275, 41775, 89075, 170050, 215950, 539900]
    sd = 12950
    inc = int(b.get())
   
    if inc in range(usbrk[0], sd):
        tax = round(ustx[0]*inc, 2)
        p = round((ustx[0]*inc) / inc * 100, 1)
        n = round(inc, 2)
    elif inc - sd in range(1, usbrk[1]):
        tax = round(ustx[1]*(inc - sd), 2)
        p = round((ustx[1]*(inc - sd)) / inc * 100, 1)
        n = round(inc - ustx[1]*(inc - sd), 2)
    elif inc - sd in range(usbrk[1], usbrk[2]):
        tax = round(995 + ustx[2]*(inc-usbrk[1] - sd), 2)
        p = round((995 + ustx[2]*(inc-usbrk[1] - sd)) / inc * 100, 1)
        n = round(inc - (995 + ustx[2]*(inc-usbrk[1] - sd)), 2)
    elif inc - sd in range(usbrk[2], usbrk[3]):
        tax = round(4664 + ustx[3]*(inc-usbrk[2] - sd), 2)
        p = round((4664 + ustx[3]*(inc-usbrk[2] - sd)) / inc * 100, 1)
        n = round(inc - (4664 + ustx[3]*(inc-usbrk[2] - sd)), 2)
    elif inc - sd in range(usbrk[3], usbrk[4]):
        tax = round(14751 + ustx[4]*(inc-usbrk[3] - sd), 2)
        p = round((14751 + ustx[4]*(inc-usbrk[3] - sd)) / inc * 100, 1)
        n = round(inc - (14751 + ustx[4]*(inc-usbrk[3] - sd)), 2)
    elif inc - sd in range(usbrk[4], usbrk[5]):
        tax = round(33603 + ustx[5]*(inc-usbrk[4] - sd), 2)
        p = round((33603 + ustx[5]*(inc-usbrk[4] - sd)) / inc * 100, 1)
        n = round(inc - (33603 + ustx[5]*(inc-usbrk[4] - sd)), 2)
    elif inc - sd in range(usbrk[5], usbrk[6]):
        tax = round(47843 + ustx[6]*(inc-usbrk[5] - sd), 2)
        p = round((47843 + ustx[6]*(inc-usbrk[5] - sd)) / inc * 100, 1)
        n = round(inc - (47843 + ustx[6]*(inc-usbrk[5] - sd)), 2)
    elif inc - sd >= usbrk[6]:
        tax = round(157804 + ustx[7]*(inc-usbrk[6] - sd), 2)
        p = round((157804 + ustx[7]*(inc-usbrk[6] - sd)) / inc * 100, 1)
        n = round(inc - (157804 + ustx[7]*(inc-usbrk[6] - sd)), 2)
    else:
        owed.config(text = "Invalid input"), perc.config(text = "null")
    owed.config(text = "$" + str(tax))
    net.config(text = "$" + str(n))
    perc.config(text = str(p) + "%")
