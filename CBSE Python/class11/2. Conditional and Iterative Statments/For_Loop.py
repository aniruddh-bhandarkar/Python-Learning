"""num=int(input("Enter a number"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)"""
num=0
for i in range(0,8):
    num=num+i
print(num)

n=int(input("number:"))
x=int(input("number:"))
sum=0
for n in range(0,n+1):
    sum=sum+x**n
print(sum)

#Print fibonacchi series
fib(n)=1
fib(n)=fib(n-1)+fib(n-2)
print(fib(n))
