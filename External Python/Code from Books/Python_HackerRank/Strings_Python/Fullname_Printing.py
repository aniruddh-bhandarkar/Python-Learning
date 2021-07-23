def print_full_name(first_name,last_name):
    print (("Hello %s %s! You just delved into python.") % (first_name, last_name))
if __name__ == '__main__':
    first_name = input("Type your name:")
    last_name = input("Type your surname:")
    print_full_name(first_name, last_name)