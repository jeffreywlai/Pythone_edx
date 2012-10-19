balance = 4773
annualInterestRate = 0.2
monthlyBalance = 0 
bal = balance 
while bal > 0 :
	j=0 
	monthlyBalance += 10 
	bal = balance 
	while j < 12 : 
		bal = (bal - monthlyBalance)*(1 + annualInterestRate/12) 
		j+=1

print ('Lowest Payment: ' + str(monthlyBalance))