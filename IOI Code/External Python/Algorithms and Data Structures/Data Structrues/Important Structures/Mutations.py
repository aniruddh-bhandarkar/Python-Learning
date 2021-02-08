def mutate_string(string, position, character):
    list2=list(string)
    list2[position]=character      
    return ''.join(list2)
if __name__ == '__main__':
    s = input()
    i,c=input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

id=input("Type your id:\n")
name=input("Type the name:\n")
sal=input("Type your Salary:\n")
str=("Id=%s\tName=%s\tSalary\t=%s" %(id,name,sal))
print(str)