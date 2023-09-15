mas = ["Орел", "Орел", "Орел", "Решка", "Решка"]
orel = 0

for coin in mas:
    if coin == "Орел":
        orel += 1

print(orel)
if orel > orel - len(mas):
    print(f"Перевернуть решку {len(mas) - orel}")
else:
    print(f"Перевернуть орлов {orel}")
