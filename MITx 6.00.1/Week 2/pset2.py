balance = 320000
annualInterestRate = 0.20
Current_Balance = float(balance)
epsilon = 0.01
low = balance/12.0
amount = 0.0
high = (balance *((1 + (annualInterestRate/12.0))**12))/12.0
MonthlyPay = (high+low)/2.0101
while abs((12*MonthlyPay)-balance) >= epsilon:
    Current_Balance = float(balance)
    
    for num in range(1, 13):
        Current_Balance = balance - MonthlyPay
        Current_Balance = Current_Balance + (Current_Balance*(annualInterestRate/12.0))
        if 12*MonthlyPay > balance:
            high = MonthlyPay
        else:
            low = MonthlyPay
        if abs(Current_Balance) < 0.01:
            break
        else:
            MonthlyPay = (high+low)/2.0101
            print(MonthlyPay)
print 'Lowest Payment: ' + str('%0.2f' % MonthlyPay) 
            
        
