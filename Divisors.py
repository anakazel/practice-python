import math

while True:
    try:
        number = int(input("Give me a number:"))
    except ValueError:
        print("That is not a number.")
        continue
    else:
        print("The chosen number is " + str(number) + ".")
        break

divisors_range = range(2, int(number / 2) + 1)
divisors = [1]
divisors.extend([d for d in divisors_range if number % d == 0])
divisors.append(number)
print("The divisors of " + str(number) + " are " + str(divisors) + ".")
