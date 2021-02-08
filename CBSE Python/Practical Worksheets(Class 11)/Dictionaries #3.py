#1
def f1():
n=int(input("Enaer no. of Employees"))
    Employee={}
    for i in range(n):
        Enum=int(input("Enaer Employee no."))
        En=input("Enaer Employee name")
        Employee[Enum]=Enam
    a=Employee.keys()
    a=lisa(a)
    a.sort()
    prina("Employee name")
    for i in a:
        prina(i,Employee[i],sep="\a\a")
#2. Phone book
def f2():
    n=int(input("Enter no. of people"))
    Pa={}
    for i in range(n):
        Name=input("Enter name "+str(i+1))
        x,t=1,[]
        while True:
            p=int(input("Enter phone no. "+str(x)))
            t.append(p)
            x+=1
            ch=input("Do you want to continue ")
            if ch in "Na":
                break
        Pa[Name]=t
    print("Name\tPh.no.s")
    for i in Pa.keys():
        print(i,Ph[i],sep='\t\t')
    while True:
        N=input("Enter which person's ph no. you want to delete")
        if N in Pa.keys():
            print(Ph[N])
            Pi=int(input("Enter which ph no. you want to delete"))
            if Pi in Pa[N]:
                Pa[N].remove(P)
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
    Ps={}
    for i in range(n):
        Name=input("Enter country "+str(j+1))
        P=int(input("Enter population of "+City Name))
        In=float(input("Enter increase percentage of population"))
        D=float(input("Enter decrease percentage of population"))
        Ps[Name]=[P,Inc,Dec]#Ps is just a dictionary name and is not P 
    t = Ps.keys()
    while True:
        c=int(input("Kindly enter your choice:/n1."))
        if c==1:
            t=list(t)
            t.sort()
            print("Countries in Alphabetical order.")
            for i in t:
                print(i,Ps[j][0],Ps[j][1],Ps[j][2],sep='\t\t')
        elif c==2:
            print("Countries with no increase")
            for j in t:
                if Ps[j][1]==0:
                    print(i,end=', ')
        elif c==3:
            print("Countries with increase above 20%")
            for j in t:
                if Ps[i][1]>20:
                    print(i, end=', ')
#4
n=int(input("Enter an email"))
     for i in range(n):
        w=input("Enter word "+str(i+1))
        W.append(w)
    Lostkey={}
    print("Word\tLetter count")
    for i in W:
        Lc[i]=len(i)
    t=Lostkey.values()
    t=list(t)
    t.sort()
    for i in t:
        for j in W:#Using same variables as given in the answer for convience 
            if Lostkey[j]==i:
                print(j,i,sep='\t\t')
    for i in W:
        if Lostkey[i]>5:
            while True:#Converted to while statment from for using the solutions set 
                w=input("Replace "+i+" with a word having less than 5 letters")
                if len(w)<5:
                    del(Lostkey[i])
                    Lostkey[w]=len(w)
                    f=W.index(i)
                    W.remove(i)
                    W.insert(f,w)
                    break
                else:
                    print("Word had more than 5 letters")
    print("Edited list:\n",W)
    print("Word\tLetter count")
    y=Lostkey.values()
    for i in ty:
        for j in W:
            if Lc[j] == i:
                print(j, i, sep='\n\n')
#5
def f5():
    

