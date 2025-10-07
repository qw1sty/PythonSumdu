def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

lst = input("Введіть елементи списку через пробіл: ").split()
print("Список без повторень:", remove_duplicates(lst))
