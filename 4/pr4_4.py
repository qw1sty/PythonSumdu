def five_min_elements(lst):
    return sorted(lst)[:5]

lst = list(map(int, input("Введіть елементи списку через пробіл: ").split()))
print("Перші 5 мінімальних елементів:", five_min_elements(lst))
