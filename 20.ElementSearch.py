def is_in_list(number_to_search, ordered_list):
    """recursive binary search."""
    # out of bounds
    if number_to_search > ordered_list[len(ordered_list) - 1] or number_to_search < ordered_list[0]:
        return False

    middle_of_list = ordered_list[int(len(ordered_list) / 2)]

    if len(ordered_list) == 1 and number_to_search != middle_of_list:
        return False

    if number_to_search == middle_of_list:
        return True
    elif number_to_search < middle_of_list:
        ordered_list = ordered_list[0: int(len(ordered_list) / 2)]
        return is_in_list(number_to_search, ordered_list)
    else:
        ordered_list = ordered_list[int(len(ordered_list) / 2): len(ordered_list)]
        return is_in_list(number_to_search, ordered_list)


the_list = [1, 2, 3, 4, 5, 6, 7]
found_in_list = is_in_list(1, the_list)
if found_in_list:
    print("Found it in the list.")
else:
    print("Did not found it in the list.")
