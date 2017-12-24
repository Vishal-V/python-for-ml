x = float(raw_input("Enter the number "))
y = x/2.0
diff = 0.01
guess = 0
while abs((y*y)-x) >= diff:
    y = y - (((y**2)-x)/(2*y))
    print(y)
    guess += 1
print 'The number of guesses is/are ' + str(guess)
print 'The answer is approximately ' + str(y)
print 'Ravindrababu Ravula'
print 'http://webcast.berkeley.edu/'