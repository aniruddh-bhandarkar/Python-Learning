# A part 2 used to calculate Simple Intrest using User's Inputs
p=int(input("Enter your Principal:"))#Input is used to take the value and by default it is in string 
r=int(input("Enter your Rate of Interest:"))#We use int() to get integral value 
t=int(input("Enter your Time:"))#Change to float for float values 
si=p*r*t/100
print("The simple Intrest is ",si)
