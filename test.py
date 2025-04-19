from G10_list import DifferenceLists

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]

print(DifferenceLists(list_1, list_2))
print(DifferenceLists(list_1, list_2, True))

print(set(list_2).difference(list_1))
print(set(list_1).difference(list_2))
