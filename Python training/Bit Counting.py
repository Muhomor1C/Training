def count_bits(n: int):
    """
    Возвращает количество единиц в двоичном представлении числа n
    """
    return str(bin(n)).count('1')


print(count_bits(1234))
