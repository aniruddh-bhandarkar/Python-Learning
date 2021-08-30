
"""def make():
    f1=open("q1.txt","w")
    n=int(input("Enter number of lines:\n"))
    for i in range(n):
        st=input("Enter a string")
        st1=st.upper()
        f1.write(st+'\n')
    f1.close()

    
def disp():
    f1=open("q1.txt")
    x=f1.read()
    print("displaying file content")
    print(x)
def disp2():
    x=input("Enter file name")
    try:
        f1=open(x)
        print()
        st=f1.read()
        st=st.upper()
        print(st)
        f1.close()
    except FileExistsError:
        print("This file does not exists")"""
def copy():
    f1=open("/Users/aniruddh/documents/Q4.txt")
    f2=open("/Users/aniruddh/documents/Q4copy.txt","w")
    for i in f1:
        lst=i.split()
        st=''.join(lst)
        f2.write(st+'\n')
    f1.close()
    f2.close()


#f1.seek() will be ignored in append(a+)mode
"""make()
disp()"""
