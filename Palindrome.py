user_input = input("Give me a string to check:")

is_palindrome = True

for i in range(0, int(len(user_input) / 2)):
    if user_input[i] != user_input[len(user_input) - i - 1]:
        is_palindrome = False

if is_palindrome:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
