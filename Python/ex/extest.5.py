if (__name__ == "__main__"):
    name_list1 = ['Aiden', 'Blair', 'Croew', 'Dback', 'Dwade', 'Flank', 'Dosh', 'Bush', 'Lesbian', 'Ryoko', 'Charoot', 'West', 'East']
    name_list2 = ['Lan', 'Sun', 'Less', 'More', 'Kevin', 'James', 'Rast', 'Downsydro', 'John', 'Jack', 'ZZ']
    name1 = Heap('Aiden')
    name2 = Heap('Lan')
    while (name_list1 != []):
        element = name_list1.pop()
        name1.insert(element)
    while (name_list2 != []):
        element = name_list2.pop()
        name2.insert(element)
    name3 = merge_heap(name1, name2)
    print(name3.BFS())
    print(first_and_last(name3))
    pass


if (size > 0):
    height = int(log(size, 2))
else:
    height = 0
# b size is the size before the last line
b_size = 0
if height > 1:
    line = 0
    while (line <= height - 1):
        b_size += pow(2, line)
        line += 1