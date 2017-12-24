x = int(raw_input("Enter a number: "))
for ans in range(0, abs(x)+1):
   if ans**3 == abs(x):
      break
if ans**3 != abs(x):
    print("The value is not a perfect cube")
else:
    if x < 0:
       print("The value is a perfect cube with cube root -" +str(ans))      
    else:
        print("The value is a perfect cube with cube root " +str(ans)) 
           
          
   