newlist=[]
newlist.append(6)
newlist.append(5)
newlist.append(10)
print(newlist)
newlist.remove(6)
newlist.append(9)
newlist.append(1)
newlist.sort()
print(newlist)
newlist.remove(10)
def reverse(newlist):
    newlist.reverse()
    return newlist
print(reverse(newlist))