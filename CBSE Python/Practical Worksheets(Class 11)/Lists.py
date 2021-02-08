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
def f2():
    L=[]
    while True:
        F=input("Enter student's first name")
        La=input("Enter student's last name")
        P=float(input("Enter percentage"))
        H=float(input("Enter height"))
        L.append([F.upper(),La.upper(),P,H])
        B=input("Do you want to continue entering? 'Y' or 'N'")
        if B=='N'or B=='n':
            break
    L.sort()
    x=1
    for i in L:
        i.insert(0,x)
        x+=1
    for i in L:
        print(i)
    while True:
        ch = int(input("Enter choice:\n1.To sort based on height\n2.To sort based on scores and display top 3"))
        if ch == 1:
            for i in range(len(L)):
                for i in range(len(L) - 1):
                    if L[i][4] > L[i + 1][4]:
                        L[i], L[i + 1] = L[i + 1], L[i]
            print("Roll no.\tFirst Name\tLast name\tPercentage\tHeight")
            for i in L:
                for j in i:
                    print(j, end="\t")
                print()
            break
        elif ch == 2:
            k = 1
            while k < len(L):
                for i in range(k):
                    if L[k][3] > L[i][3]:
                        m = L.pop(k)
                        L.insert(i, m)
                        k = k + 1
                        break
                else:
                    k+=1
            print("Top 3:")
            print("Roll no.\tFirst Name\tLast name\tPercentage\tHeight")
            for i in L[:3]:
                for j in i:
                    print(j, end="\t")
                print()
            break
        else:
            print("Please enter an appropriate option")
#Question 3
def f3():
    ch=int(input("Enter choice:\n1.Input 2 matrices and find their sum\n2.Input a matrix and find its transpose"))
    if ch==1:
        M1=[]

        r=int(input("Enter no. of rows"))
        c=int(input("Enter no. of columns"))
        print("Enter for matrix 1")
        for i in range(r):
            print("Enter for row ",(i+1))
            t=[]
            for j in range(c):
                x=int(input("Enter element "+str(j+1)))
                t.append(x)
            M1.append(t)
        print("m1:")
        for i in M1:
            print(i)
        M2=[]
        print("Enter for matrix 2")
        for i in range(r):
            print("Enter for row ",(i+1))
            t = []
            for j in range(c):
                x = int(input("Enter element " + str(j + 1)))
                t.append(x)
            M2.append(t)
        print("m2:")
        for i in M2:
            print(i)
        M3=[]
        for i in range(r):
            t=[]
            for j in range(c):
                x=M1[i][j]+M2[i][j]
                t.append(x)
            M3.append(t)
        print("Sum of m1 and m2:")
        for i in M3:
            print(i)
    elif ch==2:
        M=[]
        print("Enter matrix")
        r=int(input("Enter no. of rows"))
        c=int(input("Enter no. of columns"))
        for i in range(r):
            print("Enter for row",(i+1))
            t=[]
            for j in range(c):
                x=int(input("Enter element "+str(j+1)))
                t.append(x)
            M.append(t)
        Mt=[]
        for i in range(c):
            t=[]
            for j in range(r):
                t.append(M[j][i])
            Mt.append(t)
        print("Entered matrix:")
        for i in M:
            print(i)
        print("Transpose of the matrix:")
        for i in Mt:
            print(i)
f3()
        
