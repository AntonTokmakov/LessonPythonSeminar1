import math

# Вводим значения суммы и произведения
S = int(input("Введите сумму: "))
P = int(input("Введите произведение: "))

# Вычисляем дискриминант
D = S ** 2 - 4 * P

if D < 0:
    print("Решения нет в натуральных числах")
else:
    X = (S + math.sqrt(D)) / 2
    Y = (S - math.sqrt(D)) / 2

    if X.is_integer() and Y.is_integer() and X <= 1000 and Y <= 1000:
        print(f"X = {int(X)}, Y = {int(Y)}")
    else:
        print("Решения нет в натуральных числах")