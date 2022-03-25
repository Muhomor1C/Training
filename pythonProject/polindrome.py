forbiden = [" ", ",", ".", "-"]
text2 = []


def del_forbiden(text):
    for i in range(len(text)):
        charr = text[i]
        if charr not in forbiden:
            text2.append(charr)


def reverse(text):
    return text[::-1]


def palindrome(text):
    return text == reverse(text)


something = input("Введите текст: ")
del_forbiden(something.lower())
if palindrome(text2):
    print("Yes")
else:
    print("No")