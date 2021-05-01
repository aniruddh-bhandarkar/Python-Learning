def sort_asc_desc(di):
    val = di.values() #getting list of values
    sortval = sorted(val) #sort values by ascending order
    asc_di = {}#for holding results of the dictionary in ascending order
    desc_di = {} # for holding the result of the dictionary in descending order
    key = di.keys()# dictionary keys
    count=0
    for j in sortval:#for the first loop present 
        for i in key:
            if di[i]==j:
                asc_di[i]=j
                count+=1
                
    print(asc_di)
    print(count)
    sortval.sort(reverse = True)
    count=0
    for j in sortval:#For 
        for i in key:
            if di[i]==j:
                desc_di[i]=j
                count+=1
    print(desc_di)
    print(count)
mon = {'Z':1,'April':30,'January':31,'February':28,'March':31,'May':31}
sort_asc_desc(mon)
#p2
ompany = {}
ch = 'y'
print("Company Information")
while ch =='y' or ch ==' Y':
    cname = input("Enter Company Name:")
    cadd = input("Enter Company URL:")
    company[cname] = cadd
    ch = input("Do you want to continue:")
    if ch == 'y' or ch =="Y":
        continue
for name, url in company.items( ):
    print(name, url)
#p3
num_students = int(input("Please enter number of students:"))
student_info = {}
student_data = ['Math marks : ', 'Physics marks : ', 'Chemistry marks : ']
for i in range(num_students):
    student_name = input("Name :")
    student_info[student_name] = {}
    for entry in student_data:
        student_info[student_name][entry] = float(input(entry)) 
#storing the marks entered as integers to perform arithmetic operations later on.
#Now printing student_info
print("Please enter student name ?")
name = input("Student name : ")
if name in student_info.keys():
    print("Average student marks : ", sum(student_info[name].values())/3.0)
else:
    print("please enter valid name")



