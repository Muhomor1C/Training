def closest_mod_5(x):
    print(x)
    z = ((round(x // 5, 0)) * 5)
    print(x // 5, z)
    if z == 0:
        return x
    return "I don't know :("

print(closest_mod_5(14))
