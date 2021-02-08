n = int(input("Enter your number here :"))
list_numbers=[]
for i in range(0,n):
    list_numbers.append(i**2)
print(list_numbers)

x=int(input('Enter First number:'))
y=int(input('Enter second number:'))
print('The sum of {0} and {1} is {2}'.format(x,y,x+y))
print('The product of {0} and {1} is {2}'.format(x,y,x*y))

from numpy import *
arr=array([10,20,30,40,-50])
print("Original Array:",arr)
print("Sin values:",sin(arr))


