#program to find laragest of 3 nos
a1 = int(input("enter no:-"))
a2 = int(input("enter no:-"))
a3 = int(input("enter no:-"))
m = max(a1,a2,a3)
print(f"{m} is greatest no.")
#Write a program to find divisibilty
num=int(input("Type your number here:\n"))
num=int(input("Enter a number:"))
if num%2==0 or num%3==0 or num%7==0 or num%11==0:
print("The number is divisible by either 2,3,7 or 11")
# Write a conversion program between cm and inches
b=int(input("Type your length in cm: \n"))
if b<0:
    print("Invalid number")
else:
    b=b/2.54
    print(b)
# Write a program to input a number and check if it is a perfect square
import math
b=int(input("Type your number here:"))
if math.sqrt(b)==int:
    print("This is a perfect sqaure:")
else:
    print("Not a perfect sqaure:")

x=int(input("enter a number:"))
y=x**1/2
if y==int(y):
    print("it is a perect square")
else:
    print("it is not a perfect square")
# Income Tax
num=int(input("Type your salary "))
if num>=69000:
    num*=0.2
    print("Monthly salary is ",num)
elif  47500<=num<=68999:
    num*=0.15
    print("Monthly salary is ",num)
elif  num<=47999:
    num*=0.1
    print("Monthly salary is ",num)
else:
    print("Not high enough to be taxed!")

#WAP that accepts a character from the keyboard and determines whether it is a vowel or consonant or a number or a special symbol. Also find if it is upper case or lowercase if it is an alphabet.
if x=='a' or x=='A':
    print('it is a vowel')
elif x=='e' or x=='E':
    print('it is vowel')
elif x=='i' or x=='I':
    print('vvowel')
elif x=='o' or x=='O':
    print('vowel')
elif x=='u'or x=='U':
    print('vowel')
else:
    print('consonant')

          
