"""
Модуль, генерирующий задачи по квадратным уравнениям

Использует библиотеки math и random
Используемые: функция generate
Баги: в случае, если один из корней равен 0, вывод некорректный
Работал над модулем: Агеев Николай
Дата последнего изменения: 16.02.2021
"""
import random
import math


def generate():
    """
    Функция генерирует квадратные уравнение
    Входных параметров нет
    Вывод: 2 строки - уравнение и ответв формате упрощённой формулы
    Баги: неправильный формат вывода при нулевом корне
    """
    # устанавливаем корни
    num_1 = random.randint(-20, 20)
    den_1 = random.randint(1, 3)
    num_1 //= math.gcd(num_1, den_1)
    den_1 //= math.gcd(num_1, den_1)
    if random.random() > 0.8:
        num_2, den_2 = num_1, den_1
    else:
        num_2 = random.randint(-20, 20)
        den_2 = random.randint(1, 3)
    num_2 //= math.gcd(num_2, den_2)
    den_2 //= math.gcd(num_2, den_2)
    # форматируем ответ
    ans_1 = str(num_1) if den_1 == 1 else str(num_1) + " / " + str(den_1)
    if num_1 < 0:
        ans_1 = "- " + ans_1[1:]
    ans_2 = str(num_2) if den_2 == 1 else str(num_2) + " / " + str(den_2)
    if num_2 < 0:
        ans_2 = "- " + ans_2[1:]
    if ans_1 != ans_2:
        answer = "x_1 = {} ,  x_2 = {}".format(ans_1, ans_2)
    else:
        answer = "x = " + ans_1

    # eq_type = random.randint(1, 3)
    eq_type = 1
    if eq_type == 1:
        # считаем коеффициенты
        k_square = den_1 * den_2
        k_simple = -den_1 * num_2 - den_2 * num_1
        k_const = num_1 * num_2
        # форматируем выражение
        if k_square == 1:
            equation = "x "
        elif k_square == -1:
            equation = "- x "
        else:
            equation = str(k_square) + " x "

        if k_simple == 1:
            equation += "+ x "
        elif k_simple == -1:
            equation += "- x "
        if k_simple > 0:
            equation += "+ " + str(k_simple) + " x "
        elif k_simple < 0:
            equation += "- " + str(-k_simple) + " x "

        if k_const > 0:
            equation += "+ " + str(k_const) + " = 0"
        elif k_const < 0:
            equation += "- " + str(-k_const) + " = 0"
        # возвращаем ответ
        return equation, answer


eq, ans = generate()
print("Уравнение:", eq)
print("Ответ:", ans)
