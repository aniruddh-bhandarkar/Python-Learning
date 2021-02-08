name1="yk"
weight_kg1=76
height_m1=2.1

name2="Ani"
weight_kg2=87
height_m2=1.85

name3="Yash"
weight_kg3=65
height_m3=1.54
def bmi_calculator(name,weight_kg,height_m):
    bmi=weight_kg/(height_m**2)
    print("bmi:")
    print(bmi)
    if bmi>25:
        return name + " is  Overweight"
    else :
        return name + " is Underweight"
result1=bmi_calculator(name1,weight_kg1,height_m1)
result2=bmi_calculator(name2,weight_kg2,height_m2)
result3=bmi_calculator(name3,weight_kg3,height_m3)

print(result1)
print(result2)
print(result3)

def is_leap(year):
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    else:
        return False
