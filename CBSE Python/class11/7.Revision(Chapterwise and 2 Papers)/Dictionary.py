#Revision for Dictionary
#How to neatly print dictionaries
import json
winners={'Nihar':45,'Rohan':12,'Zeba':1,'Roshan':12,'James':16}
print(json.dumps(winners,indent=2))
#Question 1
"""Write a program that repeatedly asks the user to enter product names and prices.Store all of those in a
dictionary whose keys are the product names. When the user is done entering the products and prices,
allow them to repeatedly enter a product name and print the corresponding price or a message if the
product is not in the dictionary."""
n=int(input("_____"))
dict={}
for i in range(n):
    key=input("Product Name")
    value=(input("Price"))
    dict[key]=value
    

print("Enter product name")
print([key])
#Question 2 
"""Create a dictionary whose keys are month names and whose values are number of days in the
corresponding months.
a. Ask the user to enter the month name and use the dictionary to tell how many days are in the
month.
b. Print all the keys in alphabetical order.
c. Print the key – value pairs sorted by the number of days in each month."""
a=int(input())

#Question 3
"""Write a program that interactively creates a nested tuple to store the marks in 3 subjects for 5 students.
Create a function that computes total marks and average marks obtained by each student."""
def f1():
    d=int(input("Type in your marks"))
#Question 4
#Input a key and return its value from d.
def GET():
    d=eval(input("enter a dictionary"))
    k=int(input("enter the key"))
    x=d.get(k,"key not found") #d[k]
    if x!="key not found":
        print("the value is",x)
    else:
        print(x)
#Question 5 (Sort all the keys in descending order and print the values as per this order.)
def keys():
    d=eval(input("enter a dictionary"))
    lst=list(d.keys()) # returns all keys
    lst.sort(reverse=True) #sorting keys
    #read through the list
    for i in lst: #i is also the key of dct -d
        print("key=",i,"value=",d[i])
#Question 6(Using tuples in dictionaries)
#Question 7
a={1:"A",2:"B",3:"C"}
print(a.get(1,4))
print(a.get(5,4))






    
