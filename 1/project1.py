import math

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))


if a <= 0 or b <= 0:
    print("Помилка: числа повинні бути додатніми!")
else:
    if a < b:
        X = a / b + 1
    elif a == b:
        X = -1
    else:  # >
        X = (a * b - 5) / a

    print("Результат X =", X)
