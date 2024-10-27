def num_2() -> list:
    s = input("Введите список(элемнеты через пробел): ").split()
    number = input("Введите множитель: ")
    s2 = list()
    if number == "":
        number = 2

    try:
        number = int(number)
    except ValueError:
        print("Это не число, множитель будет равен 2")
        number = 2

    for e in s:
        try:
            elem = float(e) if '.' in e else int(e)
        except ValueError:
            elem = e
        s2.append(elem * number)

    return s2

print(num_2())
