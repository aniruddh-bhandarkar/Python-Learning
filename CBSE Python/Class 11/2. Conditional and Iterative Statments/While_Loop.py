#Even odd using for loop 
even=0
odd=0
num=int(input("Enter the maximum value:\n"))
for x in range(1,num+1):
    if(num%2==0):
        even+=x
    else:
        odd+=x
y=odd+even
print(y) 
#Factorials sums 
x=int(input("Type your value"))
factorial=1
while x>0:
    factorial*=x
    x-=1
print(factorial)
#Even odd using while loop 
num=int(input("Enter a number"))
i=1
sum1=0
sum2=0
while i<num+1:
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
        i+=1
print("Odd sum is ",sum1)
print("Even sum is",sum2)
#Sum till n numbers
num=int(input("Enter the value required"))
a=0
while num>0:
    num=num+a
    a+=1
print(a)




        
