given_list=[7,5,4,4,2,-2,-3,-5,-7]
total2=0
j=len(given_list)-1
while given_list[j]<0:
    total2+=given_list[j]
    j-=1
print(total2)
n=16
for i in range(0,n):
    print(i**2)

e2 = [x ** 2 for x in reversed(range(1, 7))]
print(e2)