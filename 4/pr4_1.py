N = int(input("Введіть кількість елементів масиву: "))
arr = []

for i in range(N):
    x = float(input(f"Введіть елемент {i+1}: "))
    arr.append(x)

positive = [x for x in arr if x > 0]

print("Додатні елементи у зворотному порядку:")
for x in reversed(positive):
    print(x, end=" ")
