x = float(raw_input("Enter the number "))
guess = 0
diff = 0.01
high = x
low = 0.0
ans = (high + low)/2
while abs((ans**2)-x) >= diff:
    guess += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print 'The answer is ' + str(ans)
print 'The number of guesses is/are ' + str(guess)