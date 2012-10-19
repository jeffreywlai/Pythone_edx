balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12.0
lower = balance/12
upper = (balance * (1 + monthlyInterestRate)**12)/12.0
guess = (lower + upper)/2
tempBalance = balance

while abs(tempBalance) >= 0.01:
    for i in range(0, 12):
        tempBalance = (tempBalance - guess) * (1 + monthlyInterestRate)
#The line under this message is the thing that fixed it for me   
    if round(tempBalance,2) == 0.01:
        print ("Lowest Payment: " + str(round(guess,2)))
        break
#The line above this message is the thing that fixed it for me
    if round(tempBalance,2) > 0.01:
        lower = guess
        i = 0
        tempBalance = balance
        guess = (lower + upper)/2
    elif round(tempBalance,2) < 0.01:
        upper = guess
        i = 0
        tempBalance = balance
        guess = (lower + upper)/2
