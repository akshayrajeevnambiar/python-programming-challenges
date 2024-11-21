# Challenge 3 : Find all items in the list
# ----------------------------------------
# Write a Python function whic woulds return all the indices of the element in
# the list. Note the list can have other list inside them.

def index_all (array: list, key: int) -> list:
    index_list = []
    for index, value in enumerate(array):
        if value == key:
            index_list.append([index])
        elif isinstance(value, list):
            for i in index_all(array[index], key):
                index_list.append([index] + i)
    return index_list

print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))