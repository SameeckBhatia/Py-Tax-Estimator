def uk(a, b, owed, perc, net):
   uktx = [0, 0.2, 0.4, 0.45]
   ukbrk = [0, 12570, 50270, 150000]
   inc = int(b.get())
   
   if inc in range(ukbrk[0], ukbrk[1]):
      tax = round(uktx[0]*inc, 2)
      p = round((uktx[0]*inc) / inc * 100, 1)
      n = inc
   elif inc in range(ukbrk[1], ukbrk[2]):
      tax = round(uktx[1]*(inc - 12570), 2)
      p = round((uktx[1]*(inc - 12570)) / inc * 100, 1)
      n = inc - (uktx[1]*(inc - 12570))
   elif inc in range(ukbrk[2], ukbrk[3]):
      tax = round(7540 + uktx[2]*(inc - ukbrk[2]), 2)
      p = round((7540 + uktx[2]*(inc - ukbrk[2])) / inc * 100, 1)
      n = inc - (7540 + uktx[2]*(inc - ukbrk[2]))
   elif inc >= ukbrk[3]:
      tax = round(52460 + uktx[3]*(inc - ukbrk[3]), 2)
      p = round((52460 + uktx[3]*(inc - ukbrk[3])) / inc * 100, 1)
      n = inc - (52460 + uktx[3]*(inc - ukbrk[3]))
   else:
      owed.config(text = "Invalid input"), perc.config(text = "null")
   owed.config(text = "£" + str(tax))
   net.config(text = "£" + str(n))
   perc.config(text = str(p) + "%")