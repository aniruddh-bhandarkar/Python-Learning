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

