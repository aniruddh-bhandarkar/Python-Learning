n = int(input())
a=int(input())
print("Type your Inputs",n)
input_integers=input()
input_list=input_integers.split()
input_list = [int(x) for x in input_list]
t=tuple(input_list)
print(hash(t))