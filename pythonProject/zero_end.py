

def zero_end(arr: list):
    """
     Упрорядочивет сприсок arr, переставляя все нули в конец
    """
    b, i = 0, 0
    while i < (len(arr) - b):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
            b += 1
        else:
            i += 1
    return arr


arr = [1, 5, 0, 0, 35, 0, 69, 7, 11, 84, 3]
print(arr)
print(zero_end(arr))
