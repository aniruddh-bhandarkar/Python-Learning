#Question 1
def f1():
    S=input("Enter your string")
    ch=input("Enter your choice\na. Check if its a palindrome\nb. Reverse each word in it\nc. Remove duplicate entries of a word entered")
    if ch=='a':
        if S==S[::-1]:
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
    elif ch=='b':
        T=S.split()
        S2=""
        for i in T:
            S2+=i[::-1]+" "
        print(S2)
    elif ch=='c':
        T=S.split()
        S2=""
        for i in T:
            if i not in S2:
                S2+=i+" "
        print(S2)
        
#Question 2
n=int(input("Enter your roll numbers")
#Question 3
def f3():
    ch=int(input("Enter choice:\n 1.Imput 2 matrices and find their sum \n"))
    if ch==1:
        M1=[]

        r=int(input("Enter no. of rows"))
        c=int(input("Enter no. of colums"))
        print("Enter for matrix 1")
        for i in range(n):
            print("Enter for row",(i+1))
            t=[]
            for j in range(c):
                x=int(input("Enter element"+str(j+1))
                t.append(x)
            M1.append(t)
            print("m1:")

                      
        for i in M1:
                      print(i)
        
