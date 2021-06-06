#print prime numbers from 1 to 20
for x in range (1, 20):
    count = 0
    for i in range(2, (x//2 + 1)):
        if(x % i == 0):
            count = count + 1
            break

    if (count == 0 and  x!= 1):
        print(" %d" %Number)
    
        
