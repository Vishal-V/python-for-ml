x = int(raw_input("Enter number: "))
if x < 0:
    neg = True
    x = abs(x)
else:
    neg = False
result = ''
if x == 0:
   print(" The answer is 0")
while x > 0:
    result = str(x%2) + result
    x = x/2
if neg == True:
    print 'The answer is -' + result
else:
    print 'The answer is ' + result
    
    
    
