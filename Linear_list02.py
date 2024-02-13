poly_array = [[7, 300], [-4, 20], [5, 0]]


def print_poly():
    global poly_array
    print("P(x) = ", end='')
    for i in poly_array:
        if i[0] > 0:
            print("+", end='')
        print(f"{i[0]}x^{i[1]}", end='')


def calculate_poly(x):
    global poly_array
    result = 0
    for i in poly_array:
        result += i[0]*pow(x, i[1])

    return result


if __name__ == "__main__":
    print_poly()
    print()
    x = int(input("X 값--> "))
    print(calculate_poly(x))
