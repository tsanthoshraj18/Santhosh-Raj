def countDigit(n): 
    count = 0
    while n != 0: 
        n //= 10
        count+= 1
    return count 
n =548
print ("% d"%(countDigit(n))) 