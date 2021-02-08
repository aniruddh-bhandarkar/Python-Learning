#Lab Activity 1


#Question 1(a) of Lab Activity 
def f1():
   n=int(input("Enter the number of lines"))
   A=65
   for i in range(1,n):
      if i==0:
        for j in range(0,n):
            print(chr(A+j),end=" ")
              
        for j in range(n-2,-1,-1):
            print(chr(A+j),end=" ")

                     
        else:
            for j in range(0,n-i):
                print(chr(A+j),end=" ")
                
            for j in range(0,i):
                print(" ",end=" ")
                
            for j in range(0,i,-1):
                print(" ",end="  ")
                
            for j in range(0,i,-1):
                print("  ",end=" ")

                
            for j in range(n-i-1,-1,-1):
                     print(chr(A+j),end=" ")
        print()
f1()      
      
#Question 1(b) of Lab Activity
def f2():
    n=int(input("Enter the no. of lines"))
    A=90
    for i in range(0,n):
        for j in range(0,i+1):
            print(chr(A-j),end="")
        print()
    for i in range(1,n+1):
        for j in range(0,n-i,-1):
            print(chr(A-i-j),end=" ")
            print(sep=" ")
f2()
#Question 2(b)
def f4():
    n=int(input("Enter no. of lines:"))
    a,b=0,1
    for i in range(1,n+1):
        for j in range(0,i):
            print(a, end=' ')
            a,b=b,a+b
        print(sep=" ")
f4()
#Question 2(c) of Lab Activity
def f5():
    a=int(input("Enter the number lines"))
    b=0
    for i in range(1,a+1):
        for j in range(0,i):
            b=j
            print(b,end=' ')
            print(sep=" ")
f5()


         

