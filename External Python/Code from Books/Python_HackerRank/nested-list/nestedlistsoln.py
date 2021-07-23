marksheet=[]
n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]
first_highest = sorted(list(set([marks for name, marks in marksheet])))[0]
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
sep = '\n'
for a,b in sorted(marksheet):
    if b == second_highest:
        print(sep.join([a]))