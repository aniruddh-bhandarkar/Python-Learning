#Prompts the user for a string

    n=input("Type a string")
    for i in range(len(n)):
        if n=='q':
            quit
        if n[i].isalpha():
            if x[i].islower():
                x[i].upper()
        elif n[i].upper():
            n[i].lower()
print(n)


