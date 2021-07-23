name='Aniruddh'
age=15 # Not a lie, I am Young
height=72 # inches
height=height*2.54
height_cm=float(format(height,'.2f')) # If you leave it with format it will take it as a string 
weight=170 # lbs
weight=weight/2.2
weight_kg=float(format(weight,'.2f'))
eyes='Black'
teeth= 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height_cm} cm  tall")
print(f"He's {weight_kg} kgs heavy")
print("Actually that's not too heavy")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the the coffee.")

# this line is tricky,try to get it exactly right
total=age+height_cm +weight_kg
print(f"If I add {age},{height_cm},and {weight_kg},I get {total}.")
