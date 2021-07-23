#1 Sum of series
"""import math
def f1():
    x=int(input("Type a number"))
    n=int(input("Type number of terms"))
    a=0
    for i in range(1,n+1,2):
        a+=(pow(x,i)/math.factorial(i))*(-1)**i
        print(a)
    p=x-a
    print(p)
f1()
#2. Tuple Operations

#3. Accept Lists
def f3():
    n=int(input("How many numbers do you want in both the lists"))
    N=[]
    D=[]
    for i in range(1,n+1):
        
        x=int(input("Enter value for numerator"))
        N.append(x)
        
        y=int(input("Enter value for denominator"))
        D.append(y)
    for j in range( N and D):
        if N[j]==D[j]:
            z=N[j]/D[j]
        else:
            print("Invalid Value")
    print(min(z))
f3()"""
#4.String Operations 
def f4():
    n=str(input("Type a sentence"))
    cvowel=0#Having capital value
    
    for i in range(0,len(n)):
        if n[i] in ('A','E','I','O','U'):
            cvowel+=1
    print(cvowel)
    print(len(n.split()))
f4()


#5.
#6. 2 Dictionaries key and value concept
#7.Matrix and finding 1) row sum 2) column sum
#8.Accept n lines from the users

                