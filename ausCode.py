def australia(a, b, owed, perc, net):
    austx = [0, 0.19, 0.325, 0.37, 0.45]
    ausbrk = [0, 18200, 45000, 120000, 180000]
    inc = int(b.get())
   
    if inc in range(ausbrk[0], ausbrk[1]):
       tax = round(austx[0]*inc, 2)
       p = round((austx[0]*inc / inc) * 100, 1)
       n = round(inc, 2)
    elif inc in range(ausbrk[1], ausbrk[2]):
       tax = round(austx[1]*(inc - ausbrk[1]), 2)
       p = round((austx[1]*(inc - ausbrk[1])) / inc * 100, 1)
       n = round(inc - (austx[1]*(inc - ausbrk[1])), 2)
    elif inc in range(ausbrk[2], ausbrk[3]):
       tax = round(5092 + austx[2]*(inc - ausbrk[2]), 2)
       p = round((5092 + austx[2]*(inc - ausbrk[2])) / inc * 100, 1)
       n = round(inc - (5092 + austx[2]*(inc - ausbrk[2])), 2)
    elif inc in range(ausbrk[3], ausbrk[4]):
       tax = round(29467 + austx[3]*(inc - ausbrk[3]), 2)
       p = round((29467 + austx[3]*(inc - ausbrk[3])) / inc * 100, 1)
       n = round(inc - (29467 + austx[3]*(inc - ausbrk[3])), 2)
    elif inc > ausbrk[4]:
       tax = round(51667 + austx[4]*(inc - ausbrk[4]), 2)
       p = round((51667 + austx[4]*(inc - ausbrk[4])) / inc * 100, 1)
       n = round(inc - (51667 + austx[4]*(inc - ausbrk[4])), 2)
    else:
       owed.config(text = "Invalid input"), perc.config(text = "null")
    owed.config(text = "A$" + str(tax))
    net.config(text = "A$" + str(n))
    perc.config(text = str(p) + "%")