print("Company: Laging Lugi")

days = (float (input("Please enter number of days worked:")))
grossPay = days * 285.00
print("Gross Pay:")
print(grossPay)

deduction = grossPay * 0.10
print("\nDeduction is 10% of Gross Pay")

netPay = grossPay - deduction
print("\nNet Pay")
print(netPay)
