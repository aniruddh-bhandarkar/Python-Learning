#1
def f1():
    n=int(input("Enter no. of employees"))
    Emp={}
    for i in range(n):
        Enum=int(input("Enter employee no."))
        Enam=input("Enter employee name")
        Emp[Enum]=Enam
    T=Emp.keys()
    T=list(T)
    T.sort()
    print("Employee's information:\nEmp.no.\tEmp.name")
    for i in T:
        print(i,Emp[i],sep="\t\t")
#2. Phone book
def f2():
    n=int(input("Enter no. of people"))
    Ph={}
    for i in range(n):
        Name=input("Enter name "+str(i+1))
        x,t=1,[]
        while True:
            p=int(input("Enter phone no. "+str(x)))
            t.append(p)
            x+=1
            ch=input("Do you want to continue?'Y' or 'N'")
            if ch in "Nn":
                break
        Ph[Name]=t
    print("Name\tPh.no.s")
    for i in Ph.keys():
        print(i,Ph[i],sep='\t\t')
    while True:
        N=input("Enter which person's ph no. you want to delete")
        if N in Ph.keys():
            print(Ph[N])
            P=int(input("Enter which ph no. you want to delete"))
            if P in Ph[N]:
                Ph[N].remove(P)
                print("Phone no. deleted")
            else:
                print("Phone number not found")
            break
        else:
            print('Please enter appropriate name')
    print("Edited phone book:\nName\tPh.no.s")
    for i in Ph.keys():
        print(i,Ph[i],sep="\t\t")
 
#3. Write a program to input the following date for ‘n’ years: population of corresponding cities along with increase and decrease percentage.
def f3():
    n=int(input("Enter how many countries"))
    Pop={}
    for i in range(n):
        Name=input("Enter country "+str(i+1))
        P=int(input("Enter population of "+Name))
        Inc=float(input("Enter increase percentage of population"))
        Dec=float(input("Enter decrease percentage of population"))
        Pop[Name]=[P,Inc,Dec]
    t = Pop.keys()
    while True:
        ch=int(input("Enter choice:\n1. Display all country details in alphabetical order\n2. Display all countries with no increase\n3. Display all countries with increase above 20%"))
        if ch==1:
            t=list(t)
            t.sort()
            print("Country\tPopulation\tInc\tDec")
            for i in t:
                print(i,Pop[i][0],Pop[i][1],Pop[i][2],sep='\t\t')
        if ch==2:
            print("Countries with no increase")
            for i in t:
                if Pop[i][1]==0:
                    print(i,end=', ')
        if ch==3:
            print("Countries with increase above 20%")
            for i in t:
                if Pop[i][1]>20:
                    print(i, end=', ')
        C=input("\nDo you want to continue entering choices? 'Y' or 'N'")
        if C in "Nn":
            break
#4.
def f4():
    n=int(input("Enter how many words"))
    W=[]
    for i in range(n):
        w=input("Enter word "+str(i+1))
        W.append(w)
    Lc={}
    print("Word\tLetter count")
    for i in W:
        Lc[i]=len(i)
    t=Lc.values()
    t=list(t)
    t.sort()
    for i in t:
        for j in W:
            if Lc[j]==i:
                print(j,i,sep='\t\t')
    for i in W:
        if Lc[i]>5:
            while True:
                w=input("Replace "+i+" with a word having less than 5 letters")
                if len(w)<5:
                    del(Lc[i])
                    Lc[w]=len(w)
                    f=W.index(i)
                    W.remove(i)
                    W.insert(f,w)
                    break
                else:
                    print("Word had more than 5 letters")
    print("Edited list:\n",W)
    print("Word\tLetter count")
    t=Lc.values()
    for i in t:
        for j in W:
            if Lc[j] == i:
                print(j, i, sep='\t\t')
