n = int(input("Введите число: "))

for i in range(n + 1):
    if 2 ** i <= n:
        print(2**i)
    else:
        break