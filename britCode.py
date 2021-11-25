def uk(a, b, owed, perc):
   uktx = [0, 0.2, 0.4, 0.45]
   ukbrk = [0, 12570, 50270, 150000]
   c = a.get()
   inc = int(b.get())
   
   if inc in range(ukbrk[0], ukbrk[1]):
      tax = round(uktx[0]*inc, 2)
      p = round((uktx[0]*inc) / inc * 100, 1)
   elif inc in range(ukbrk[1], ukbrk[2]):
      tax = round(uktx[1]*(inc - 12570), 2)
      p = round((uktx[1]*(inc - 12570)) / inc * 100, 1)
   elif inc in range(ukbrk[2], ukbrk[3]):
      tax = round(7540 + uktx[2]*(inc - ukbrk[2]), 2)
      p = round((7540 + uktx[2]*(inc - ukbrk[2])) / inc * 100, 1)
   elif inc >= ukbrk[3]:
      tax = round(52460 + uktx[3]*(inc - ukbrk[3]), 2)
      p = round((52460 + uktx[3]*(inc - ukbrk[3])) / inc * 100, 1)
   else:
      owed.config(text = "Invalid input"), perc.config(text = "null")
   owed.config(text = "£" + str(tax))
   perc.config(text = str(p) + "%")