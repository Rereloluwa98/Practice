
co = int(input("What do you have left in pesos?"))
pe = int(input("What do you have left in soles?"))
br = int(input("What do you have left in reais?"))

total_co = co * 0.0002448
total_pe = pe * 0.2759
total_br = br * 0.01770

"""
print("You have $",co * 0.0002448 )
print("You have $",pe * 0.2759)
print("You have $",br * 0.01770)
"""
total = total_co + total_pe + total_br
print("Cha-ching!. Your total is : $",total)