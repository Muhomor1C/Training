def multiply(number: int):
    count_digits = len(str(abs(number)))
    return number * 5 ** count_digits




print(multiply(3)) #==15 # 3 * 5¹
print(multiply(10)) #==250 # 10 * 5²
print(multiply(200)) #==25000 # 200 * 5³
print(multiply(0)) #==0 # 0 * 5¹
print(multiply(-3)) #==-15 # -3 * 5¹
