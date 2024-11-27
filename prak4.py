def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))


def sort_list(unique_list):
    numbers = sorted([x for x in unique_list if isinstance(x, int)])
    strings = sorted([x for x in unique_list if isinstance(x, str)])
    return numbers + strings


input_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
unique_list = remove_duplicates(input_list)
print("Список без повторень:", unique_list)


sorted_list = sort_list(unique_list)
print("Відсортований список:", sorted_list)
