sentence = input("Введіть речення: ")

words = sentence.split()
count = 0

for word in words:
    if word.endswith("р"):
        count += 1

print("Кількість слів, які закінчуються на 'р':", count)