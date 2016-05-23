import random

list1 = random.sample(range(1, 60), 20)
list2 = random.sample(range(40, 98), 20)

set1 = set(list1)
set2 = set(list2)

common_list = set1.intersection(set2)

print("The common list is " + str(list(common_list)) + ".")