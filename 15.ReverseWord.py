def reverse_list(the_list):
    rev_user_input = []
    for i in range(0, len(the_list)):
        rev_user_input.append(user_input.pop())
    return rev_user_input


user_input = input("What is the text?:")
user_input = list(user_input)
print(reverse_list(list(user_input)))


