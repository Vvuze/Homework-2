def summ(a, b):
    return a + b


def minus(a, b):
    return a - b


def delen(a, b):
    if b == 0:
        raise Exception("Деление на 0")
    else:
        return a / b


def stepen(a, b):
    return a ** b


def mnozh(a, b):
    return a * b


def oper():
    message = '''
                Выберете математическую операцию:

                + : Сложение
                - : Вычитание
                / : Деление
                * : Умножение
                ^ : Степень
                # : Выход
                Ваш выбор:
                '''
    operations = '+-/*^#'
    operation = input(message)
    while operation not in operations:
        print('Такой операции нет')
        operation = input(message)
    return operation


def calc():
    while True:
        try:
            a = int(input("Введите первое число: "))
        except:
            raise ValueError("Wrong datatype")

        try:
            b = int(input("Введите второе число: "))
        except:
            raise ValueError("Wrong datatype")

        s = oper()
        if s == '+':
            print("Результат: ", summ(a, b))
        elif s == '-':
            print("Результат: ", minus(a, b))
        elif s == '*':
            print("Результат: ", mnozh(a, b))
        elif s == '/':
            if b == 0:
                raise Exception("Деление на ноль")
            else:
                print("Результат: ", delen(a, b))
        elif s == '^':
            print("Результат: ", stepen(a, b))
        else:
            exit()


calc()
