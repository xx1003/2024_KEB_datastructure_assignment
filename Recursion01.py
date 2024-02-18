deci = int(input("10진수 입력 --> "))


def deci_to_binary(d):
    if d < 2:
        return str(d)

    return deci_to_binary(d // 2) + str(d % 2)


def deci_to_octal(d):
    if d < 8:
        return str(d)

    return deci_to_octal(d // 8) + str(d % 8)


def deci_to_hex(d):
    if d < 16:
        if d > 9:
            return chr(55 + d)
    elif d % 16 > 9:
        return deci_to_hex(d // 16) + chr((d % 16) + 55)
    else:
        return deci_to_hex(d // 16) + str(d % 16)


print(f"2진수 : {deci_to_binary(deci)}")
print(f"8진수 : {deci_to_octal(deci)}")
print(f"16진수 : {deci_to_hex(deci)}")