print("Please think of a number between 0 and 100!")
high = 100
low = 0
ans = (high + low)/2
x = ''
while x != 'c':
    print ('Is your secret number ' +str(ans) + '?')
    x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if x == 'h':
        high = ans
    elif x == 'l':
        low = ans
    elif x == 'c':
        print 'Game over. Your secret number was: ' + str(ans)
        break
    else:
        print 'Sorry, I did not understand your input.'
    ans = (high + low)/2
                  
    