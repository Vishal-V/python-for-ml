mmp = ''
balance = 4842
total = ''
rembal = ''
bal = ''
total = 0.0
monthlyPaymentRate = 0.04
annualInterestRate = 0.2
for num in range(1,13):
    print 'Month: ' + str(num)
    mmp = (monthlyPaymentRate)*balance
    total = total + mmp
    print 'Minimum monthly payment: ' + str('%.2f' % mmp)
    rembal = (balance - mmp) 
    bal = rembal + ((annualInterestRate/12.0)*rembal)
    print 'Remaining balance: ' + str('%.2f' % bal)
    balance = bal
print 'Total paid: ' + str('%.2f' % total)
print 'Remaining balance: ' + str('%.2f' % bal)