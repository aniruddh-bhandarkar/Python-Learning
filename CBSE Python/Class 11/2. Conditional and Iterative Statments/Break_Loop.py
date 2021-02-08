#Divisors of a number
N=(int)(input("Enter Number: "))
for x in range(1,N+1):
   if (N%x==0):
       print(x)
#More efficent code
n=int(input("Enter Number:"))
mid=n/2
print('the divisors',n)
for a in range(2,mid+1):
    if n%a==0:
        print(a)
#To test if a number is a prime or not
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
#Print numbers b/w 1 to 20, if the number is 0 or a charcater it must exist
n=int(input("Enter your number"))
while 1<n<20:
    print("Your number is ",n)
else:
     if n==char:
         print("Invalid charcater")


    

       
