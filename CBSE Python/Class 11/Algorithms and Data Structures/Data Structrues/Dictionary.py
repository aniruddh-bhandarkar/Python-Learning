d={}

d['xyz']=123
d['abc']=345
#Self-Explantory Things 
print(d)
print(d.keys())
print(d.values())
#Map Values
def cube(x):
    return x**2
cubes=map(cube,range(10))
print(cubes)
#Lambda Values
print(lambda x:x**2)(5) # Maps

print(lambda x,y)
