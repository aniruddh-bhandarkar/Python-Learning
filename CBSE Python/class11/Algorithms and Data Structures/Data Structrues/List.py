"""Few useful properties of List
1.Lists need not be homogenous,can contain strings,integers...
2.They are mutuable and can be altered
3.The elements in a List are indexed
4.Elements of list can be duplicated
5.They can be easily created without calling a function """

List=[]
print("Blank List:")
print(List)

List=[10,20,14]
print("\nList of numbers :")
print(List)

# A Multidimensional List
List=[['Geeks','For'],['Geeks']]
print('\nMulti-Dimensional List')
print(List)

#Creating a List with Duplicate number
List1=[1,7,8,9,54,6,7,7,8,8,8]
print("\nList with the use of Numbers: ") 
print(List1)

# Size of a List
List2=[10,2,3,4]
print(len(List2))

#Append of List
List=[]
print("Intial Blank List:")
print(List)

List.append(1)
List.append(3)
print("\nList after addition of element")
print(List)

#Slicing Operation
List4=['A','N','I','R','U','D','D','H']
print(List4)
#Few examples
Sliced_List=List4[5:]
print(Sliced_List)

Sliced_List=List4[::-1]#Reverses the order of the list
print(Sliced_List)

#List Comphrensions
