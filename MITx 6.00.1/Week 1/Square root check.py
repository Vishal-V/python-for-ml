x = float(raw_input("Enter number: "))
Guess = 0
diff = 0.01
step = diff**2
ans = 0.0
while abs(ans**2 - x) >= diff and ans <= x :
    Guess += 1
    ans += step
print "The number of guesses is " + str(Guess )
if abs(ans**2 - x) > diff :
    print("Could not compute")
else:
    print(str(ans) + 'is close to the square root of' + str(x))
    
    
