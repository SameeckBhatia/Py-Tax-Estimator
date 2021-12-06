def canada(a, b, owed, perc, net):
    cantx = [0.15, 0.205, 0.26, 0.29, 0.33]
    canbrk = [0, 49020, 98040, 151978, 216511]
    sd = 13229
    inc = int(b.get())
   
    if inc in range(canbrk[0], sd):
        tax = round(cantx[0]*inc, 2)
        p = round((cantx[0]*inc) / inc * 100, 1)
        n = inc - (cantx[0]*inc)
    elif inc - sd in range(1, canbrk[1]):
        tax = round(cantx[0]*(inc - sd), 2)
        p = round((cantx[0]*(inc - sd)) / inc * 100, 1)
        n = inc - (cantx[0]*(inc - sd))
    elif inc - sd in range(canbrk[1], canbrk[2]):
        tax = round(7353 + cantx[1]*(inc-canbrk[1] - sd), 2)
        p = round((7353 + cantx[1]*(inc-canbrk[1] - sd)) / inc * 100, 1)
        n = inc - (7353 + cantx[1]*(inc-canbrk[1] - sd))
    elif inc - sd in range(canbrk[2], canbrk[3]):
        tax = round(17402 + cantx[2]*(inc-canbrk[2] - sd), 2)
        p = round((17402 + cantx[2]*(inc-canbrk[2] - sd))/ inc * 100, 1)
        n = inc - (17402 + cantx[2]*(inc-canbrk[2] - sd))
    elif inc in range(canbrk[3], canbrk[4]):
        tax = round(31426 + cantx[3]*(inc-canbrk[3] - sd), 2)
        p = round((31426 + cantx[3]*(inc-canbrk[3] - sd)) / inc * 100, 1)
        n = inc - (31426 + cantx[3]*(inc-canbrk[3] - sd))
    elif inc - 12298 >= canbrk[4]:
        tax = round(50140 + cantx[4]*(inc-canbrk[4] - 12298), 2)
        p = round((50140 + cantx[4]*(inc-canbrk[4] - 12298)) / inc * 100, 1)
        n = inc - (50140 + cantx[4]*(inc-canbrk[4] - 12298))
    else:
        owed.config(text = "Invalid input"), perc.config(text = "null")
    owed.config(text = "C$" + str(tax))
    net.config(text = "C$" + str(n))
    perc.config(text = str(p) + "%")