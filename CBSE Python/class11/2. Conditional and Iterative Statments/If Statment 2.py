#Program 1
"""deposit=int(input("Enter the amount deposited"))
years=int(input("Enter the duration of deposit"))
if deposit<=2000 and years>2:
    I=deposit"""
#Program 2
a= int(input("value of a:\n"))
b= int(input("value of b:\n"))
c= int(input("value of c:\n"))
d= b**2-4*a*c
d=d**0.5
r1=0
r2=0
if d <0:
    print("Not valid number")
else:
    if d==0:
        r1=-(b)/2*a
        print("the roots are:\n",r1)
    elif d >0:
        r1=-b+d/2*a
        r2=-b-d/2*a
        print("the roots are:\n",r1,r2)

