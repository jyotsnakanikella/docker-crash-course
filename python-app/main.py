n = int(input("please enter any positive number:"))

if n<0:
    print("error: number must be positive")
    
else:
    sum = 0
    i = n
    
    while i>0:
        sum+=i
        i-=1
        
    print("sum of all numbers till",n," is ",sum)    
        
            