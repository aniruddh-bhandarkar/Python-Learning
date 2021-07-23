#Queues
a=[]
def push_queue(element):
    a.append(element)
def pop_queue():# No need to define any element as python knows
    if len(a)<=0:
        print("Not Valid list")
    else:
        return a.pop(0)
def display_queue():
    for i in range(len(a)-1,-1,-1):
        print(a[i],end=" ")
    print()
push_queue(23)
display_queue()
push_queue(12)
display_queue()
pop_queue()
