x = float(raw_input("Enter a number: "))
diff = 0.01
step = diff**2
guesses = 0
ans = 0.0
while ans <= x:
    if abs((ans**2) - x) <= diff:
        break
    else:
        ans += step
        guesses += 1
if ans > x:
    print 'Failed operation'
else:
    print 'The answer is ' + str(ans)
    print 'The number of guesses is/are ' + str(guesses)
