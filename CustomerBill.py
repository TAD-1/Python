totalSales = float (input(("Amount tendered: ")))

serviceCharge = totalSales * 0.15
print("\nService Charge")
print(serviceCharge)

service = totalSales + serviceCharge

addedTax = totalSales * 0.10
print("\nTax")
print(addedTax)

tax = totalSales + addedTax


total = totalSales + service + tax 
print("\nGross Bill:")
print(total)

customerPayment = float (input(("\nPayment: ")))
change = total - customerPayment

print("\nChange: ")
print(change)
