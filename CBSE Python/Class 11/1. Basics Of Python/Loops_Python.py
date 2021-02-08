#Length of i
for i in range(0,98,2):
    print(i)

#Multiplication Tables
for i in range(1,11):
    print(3,'x',i,'=',3*i)
#While loops Printing Factorials
n=5
temp=n
fac=1
while temp>0:
    fac*=temp
    temp-=1
print('Factorial of ',n,'is',fac)

#Break,Continue,Pass
#Pass do it later
for i in range(10):
    if i==5:
        continue
    print(i)
    




