languages=["c","c++","perl","Python"]
for x in languages:
    print(x)
# Write a program for finding sum and average 
l=[10,20,12,2,23,9]
s=0
avg=0
for i in range(len(l)):
    s+=l[i]
    avg=s/len(l)
print(s)
print(avg)
l.count(20)
#Lists are mutable;Joining the lists
l=[]
for i in range(50):
    l.append(i*i)
print(l)
#Program 3
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v
print(fun(data[0]))
#Dictionary Q
my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4

sum = 0
print(my_dict)
for k in my_dict:
    sum += my_dict[k]
    print(my_dict[k])
print (sum)
