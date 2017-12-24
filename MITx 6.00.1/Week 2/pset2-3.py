balance = 320000
annualInterestRate = 0.20
balance1 = balance
low = balance / 12
high = (balance * (1 + annualInterestRate / 12)** 12) / 12.0
mmp = round((high + low) / 2, 2)

while True:
    
    for num in range(1, 13):
       balance2 = balance1 - mmp
       balance1 = round((balance2 + balance2*(annualInterestRate)/12.0), 2)
    
    if abs(balance1) < 0.01:
        print 'Lowest Payment: ' + str(round((mmp), 2))
        break
    else:
        if balance1 > 0:
            low = mmp
        elif balance1 < 0:
               high = mmp
        mmp = (high + low) / 2
        balance1 = balance
        
            
    
    
