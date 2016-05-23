from random import randint

def generate_password(length):
    password = ''
    for i in range(0, length):
        password += (chr(randint(33, 127)))
    return password


while True:
    try:
        length = int(input("What is the length of the password?"))
    except ValueError:
        print("That is not a number.")
    else:
        print("The generated password is " + generate_password(length) + ".")
        break
