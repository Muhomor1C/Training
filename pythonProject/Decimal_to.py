def qwestion(numeric_system, digit):
    """
    Возвращает число digit, в системе счиления numeric system до 36-ричной
    :param numeric_system: numeric system
    :param digit: decimal digit
    :return: digit in numeric system
    """
    answer = []
    digits = [chr(i) for i in range(48, 91) if i not in range(58, 65)]


    def raschet(numeric_system, digit):
        if digit < numeric_system:
            answer.insert(0, digits[digit])
        else:
            answer.insert(0, digits[digit % numeric_system])
            digit = digit // numeric_system
            return raschet(numeric_system, digit)

    raschet(numeric_system, digit)
    return answer


print(*qwestion(16, 15000))
