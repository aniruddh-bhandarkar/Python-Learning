n = int(input())
arr = map(int, input().split())
newlist=[]
a=sorted(arr)
p=max(a)
for e in a:
    if e!=p:
        newlist.append(e)
print(max(newlist))