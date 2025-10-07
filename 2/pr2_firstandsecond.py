import math

def calc_z(alpha):
    return math.cos(alpha)**2 + math.cos(alpha)**4

def need_money(stipend, costs):
    total_stipend = stipend * 10
    total_costs = 0
    current_costs = costs
    for _ in range(10):
        total_costs += current_costs
        current_costs *= 1.05
    return total_costs - total_stipend

if __name__ == "__main__":
    alpha = float(input("Введіть значення α (у радіанах): "))
    z = calc_z(alpha)
    print("Результат обчислення z =", z)

    A = float(input("Введіть розмір стипендії (грн): "))
    B = float(input("Введіть витрати на проживання (грн): "))
    money = need_money(A, B)
    print("Сума грошей, яку треба попросити в батьків:", round(money, 2), "грн")
