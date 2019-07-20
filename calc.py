# command line input:
# python calc.py [property value as int] [yearly interest rate as float] [downpayment as int] [term of loan as int]

# sample input:
# python calc.py 350000 3.2 70000 25

import sys

interest = float(sys.argv[2]) / 12 / 100
borrowed = float(sys.argv[1]) - float(sys.argv[3])
term = float(sys.argv[4]) * 12

monthlyPayment = borrowed / ((((1 + interest) ** term) - 1) / (interest * (1 + interest)**term))
print("Monthly Payment:", round(monthlyPayment, 2))

totalPayment = monthlyPayment * term
print("Total Payment:", round(totalPayment, 2))

totalInterest = totalPayment - borrowed
print("Total Interest:", round(totalInterest, 2))