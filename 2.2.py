multiply_lambda = lambda elements_str, multiplier: [
    (float(e) if '.' in e else int(e)) * multiplier if e.replace('.', '', 1).isdigit() else e * int(multiplier)
    for e in elements_str.split()
]

data = input("Введите элементы через пробел (числа и строки): ")
multiplier = input("Введите множитель (по умолчанию 2): ")
if multiplier == "":
    multiplier = 2
else:
    try: multiplier = int(multiplier)
    except:
        print("Это не число, множитель будет равен 2")
        multiplier = 2

result = multiply_lambda(data, multiplier)
print("Результат:", result)
