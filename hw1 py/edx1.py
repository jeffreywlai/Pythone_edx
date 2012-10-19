balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 0 
totalPaid = 0
while month < 12:
	minPaid = round((balance * monthlyPaymentRate), 2)
	newbalance = round((balance - minPaid), 2)
	interest = round(newbalance * (annualInterestRate / 12), 2)
	balance = round(newbalance + interest, 2)
	totalPaid = totalPaid + minPaid
	month += 1
	print ('Month: ' + str(month))
	print ('Minimum monthly payment: ' + str(minPaid))
	print ('Remaining balance: ' + str(balance))

print ('Total Paid: ' + str(totalPaid))
print ('Remaining balance: ' + str(balance))
