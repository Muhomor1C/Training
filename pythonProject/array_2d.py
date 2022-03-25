def create_2d_array(m, n):
    array = []
    check = 1
    for i in range(m):
        ethernal_array = []
        for z in range(n):
            ethernal_array.append(check)
            check += 1
        array.append(ethernal_array)
    return array


def swap(array, i, u):
    array[i], array[u] = array[u], array[i]


def change_to_mirror(array):
    for array2 in array:
        for i in range(len(array2) // 2):
            u = len(array2) - 1 - i
            swap(array2, i, u)


def print_array(array):
    for x in range(len(array)):
        for z in range(len(array[x])):
            print(array[x][z], end=' ')
        print('')


def print_array_mirror(array):
    for x in range(len(array)):
        for z in range(len(array[x]) - 1, -1, -1):
            print(array[x][z], end=' ')
        print('')


def print_all():
    print_array(a)
    print()
    print_array_mirror(a)
    print()


a = create_2d_array(3, 3)
print_all()

change_to_mirror(a)
print_all()
