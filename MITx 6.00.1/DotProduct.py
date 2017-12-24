listA = [1, 2, 3]
listB = [4, 5, 6]
def dotProduct(listA, listB):
    x = 0
    result = 0

    while x != len(listA):
        result += listA[x] * listB[x]
        x += 1
    return result    
    