def duplicate_count(text):
    text_lower = text.lower()
    count_doblecharasters = 0
    finded_double_charasters = []
    text_len = len(text_lower)

    for i in range(text_len):
        text_symbol = text_lower[i:i+1]
        text_worked = text_lower[i:len(text_lower)]
        if text_worked.count(text_symbol) > 1:
            if finded_double_charasters.count(text_symbol) < 1:
                finded_double_charasters.append(str(text_symbol))
                count_doblecharasters += 1
    return count_doblecharasters


def duplicate_count_2(text):
    text_lower = list(text.lower())
    text_len = len(text_lower)
    text_lower.sort()
    count_doblecharasters = 0
    i = 0
    while i < text_len:
        text_symbol = text_lower[i]
        count_charasters = text_lower.count(text_symbol)
        if count_charasters > 1:
            i += count_charasters
            count_doblecharasters += 1
        else:
            i += 1
    return count_doblecharasters



print('abcde: ' + str(duplicate_count2('abcde')))
print('aabbcde: ' + str(duplicate_count2('aabbcde')))
print('aabBcde: ' + str(duplicate_count2('aabBcde')))
print('indivisibility: ' + str(duplicate_count2('indivisibility')))
print('Indivisibilities: ' + str(duplicate_count2('Indivisibilities')))
print('aA11: ' + str(duplicate_count2('aA11')))
print('ABBA: ' + str(duplicate_count2('ABBA')))