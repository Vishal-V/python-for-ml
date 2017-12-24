mmp = 0
balance = 4773
annualInterestRate = 0.2
total = 0
rembal = 0.0
bal = 0.0
balance1 = balance
while balance1 > 0:
    balance1 = balance
    total = 0
    rembal = 0.0
    bal = 0.0
    mmp += 10
    for num in range(1, 13):
       total = mmp * 12
       rembal = (balance1 - mmp)
       bal = rembal + ((annualInterestRate/12.0)*rembal)
       balance1 = bal
    if balance1 <= 0:
        break
        
print 'Lowest Payment: ' + str('%i' % mmp) 
    

    
    