x = float(raw_input("Enter number between 0 and 1 : "))
p = 0
while ((2**p)*x) % 1 != 0 :
    p += 1
num = int((2**p)*x)
if num == 0:
    print("The binary is 0")
result = ''
while num > 0:
    result = str(num%2) + result
    num = num/2
for i in range(p - len(result)):
    result = '0' + result
result = result[0 : -p] + '.' + result[-p : ]
print result 
