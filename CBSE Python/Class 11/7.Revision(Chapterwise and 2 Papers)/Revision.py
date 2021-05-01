#Write a Python Program to Read a List of Words and Return the Length of the Longest One
def f1():
    lit=[]
    x=int(input("Enter the number of words you require"))
    for i in range(x):
        n=str(input("Enter a word"))
        lit.append(n)
    a=max(lit)
    print(a)
def max(lit):
    high=lit[0]
    for i in range(len(lit)):
        if len(lit[i]) >= len(high):
            high = lit[i]
    
    return high 
f1()
  




    