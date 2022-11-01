'''
1. Gain = Selling Price(S.P.) - Cost Price(C.P)
2. Loss = Cost Price (C.P.) - Selling Price (S.P)
3. Gain % = Gain x 100 / C.P
4. Loss % = Loss x 100 / C.P
5. S.P. = [(100 + Gain%)/100] x C.P
6. S.P. = [(100 - Loss%)/100] x C.P
7. C.P. = [100/ (100 + Gain%) ] x S.P
8. C.P. = [100/ (100 - Loss%) ] x S.P

9. simple.Interest = PNR/100
10. amount = p[1+(rt/100)]
'''

name = input("enter your name: ")
#int()
selling_price = int(input("selling price: "))
cost_price = int(input("Cost price: "))
gain = selling_price - cost_price #arithemetic operator
gain_percent = gain * 100 / cost_price
print(name,"got",gain_percent,"percentage gain")

#it's raining
print('it\'s raining')
#c:\desktop\name
print('c:\desktop\\name')

print((-4)**2)
