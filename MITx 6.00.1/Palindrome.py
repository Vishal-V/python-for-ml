def isPal(pal):
    while True:
        if pal == '':
            return True
        if len(pal) == 1:
            return True
        if len(pal) == 2: 
            if pal[0] == pal[-1]:
                return True  
        if pal[0] == pal[-1]:       
            pal = pal[1:-1]
            
        else:
            return False 
            break
        return True
        
def isPalindrome(aString):
    pal = ''
    aString = aString.lower()
    for char in aString:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            pal += char
    return isPal(pal)
    
