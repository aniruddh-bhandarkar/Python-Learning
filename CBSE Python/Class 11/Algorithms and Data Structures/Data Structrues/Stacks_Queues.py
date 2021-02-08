#Stacks 
a=[]
def push_stack(element):
    a.append(element)
def pop_stack():# No need to define any element as python knows
    if len(a)<=0:
        print("Not Valid list")
    else:
        return a.pop()
def display_stack():
    for i in range(len(a)-1,-1,-1):
        print(a[i],end=" ")
    print()

push_stack(23)
display_stack()
push_stack(21)
display_stack()
pop_stack()
display_stack()





