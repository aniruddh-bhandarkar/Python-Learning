
def f1():
    s=" FooT BaLl " #this string has 3 spaces at
#beginning and end of string
    st1=s.lstrip()
    for i in range(0,len(st1)-1):    
        x=st1[i]
    print(x)
    if not(x.isspace() and i%2==0):
        print(i,x.lower())

    st1=st1.replace('oo','?')
    print(st1)
f1()

def f2():
            lst=[5,4,3,2,1]
            c1=len(lst)
            print(c1)
            tmp=[]
            for j in range(c1-1):
                print(j)
            if j%2==1 and j==c1-2:
                lst.reverse()
            if lst[j+1]<=lst[j]+2:
            tmp.append(lst[j])
print (lst,tmp)
f2()
def f4():
    tp=(1,2,3,4)
    dct={}
    for i in tp:
        dct[i]=i+10
        m=min(tp)
        dct['m']=m
        for k in dct:
            if type(k)==int:
                if k>3:
                  print(k,dct[k], end=' ')
        print(dct)
        print(len(tp)+len(dct))
        tp1=tuple(sorted(tp,reverse=True))
        print(tp,tp1)
f4()

'''
# Syntax error correction functions
def f4():
    text="student"
    dct={'0':100,'0':200,'2':300,'3':400}
    c=0
    for i in range(len(dct)):
        if text.islower():
            dct[i]=text[i].upper()
            c+=1
        if text.split():
            break
        dct.pop(1)
        pos=dct.update(text[0],text[1])

f4()
'''
'''def f3():
    L=[1,"A",2,"B"]
    t=(1,11,111)
    x=0
    i=0
    if t[i] in (0,3):
        while i<len(L):
            if L[i]<5:
                t.count(i)
            else:
                t[i]+=L[i]+2
                i+=2
        L[0].extend(t[1])
        if L[1]>100:
            print (L[3])
            L.pop(-10)
f3()
'''
'''
print("Hello world")
ui={}
ja={"Mar":12}
def f2():
    st1='' #empty string
    st2=" true "
    L=[st2,1,2,3]
    print(st2+L[0].lstrip("abc"))
    if L[1]>0:
        if st2.isspace():
            st1+=st2                                                            
        for i in range(len(L)):
            if type(len(L))!=int:
                continue
        L[i]+=10
    else:
        print(L)
f2()

'''

