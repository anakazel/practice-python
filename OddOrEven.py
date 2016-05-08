#http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

while True:
    try:
        number = int(input("Give me a number to check:"))
        divide = int(input("Give me a number to divide by:"))
    except ValueError:
        print("That is not a number.")
        continue
    else:
        print("The chosen number is " + str(number) + ".")
        print("The number to divide by " + str(number) + ".")
        break

if number % 4 == 0:
    print("The number is divisible by 4.")
elif number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

if number % divide == 0:
    print(str(number) + " divides evenly by " + str(divide) + ".")
else:
    print(str(number) + " does not divide evenly by " + str(divide) + ".")