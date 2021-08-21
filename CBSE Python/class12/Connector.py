
from datetime import datetime
import mysql.connector as m


def q1(): # display table structure
    cursor=con.cursor() #creating cursor instance
    cursor.execute('desc t1')
    data=cursor.fetchall()

    for i in data:
        print(i)

def q2():
    cursor=con.cursor()
    st="select name,dt from t1 where dt like '2020%'"
    cursor.execute(st)
    data=cursor.fetchall()

    for i in data:
        print(i)

#main here
#creating connection object
con=m.connect(host='localhost', user='root', passwd='SGROKX2k20',database='test')
if m:
    print("success")
else:
    print("error")
while 1:
    ch=int(input("choose 1 or 2, 0 to stop"))
    if ch==1:
        q1()
    elif ch==2:
        q2()
    elif ch==0:
        break
def q5():
    cursor=con.cursor()
    st='select * from t1'
    cursor.execute(st)    
    data=cursor.fetchmany(2)
    cnt=cursor.rowcount
    print("total number of rows=",cnt)
    for i in data:
        print(i)
    data=cursor.fetchmany(1)
    cnt=cursor.rowcount
    print("total number of rows=",cnt)
    for i in data:
        print(i)
def q6():#parameterized -old style (%s), new(.format)
    cursor=con.cursor()
    x=int(input('enter value'))
    y=input('enter name')
    st='select * from t1 where value>%s and name="%s"' %(x,y)
    #st='select * from student where value>{x} and name="{y}"'.format(x,y)
    cursor.execute(st)
    data=cursor.fetchall()

    for i in data:
        print(i)
    
#Formatted strings questions 
def f7():
    y=input("Enter the letter")
    "select name from t1 where name like %s"%(y+'%')
    st='select name from t1 where name like %s%'#1.(Starting with % and formatting is s%)
    st='select values from t1 where values=(x,y) order by values'#2.
    st='select dates from t1 where values>s%'#3.
    
