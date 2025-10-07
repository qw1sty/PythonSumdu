import math
import student_module

def calc_z(alpha):
    return math.cos(alpha)**2 + math.cos(alpha)**4

if __name__ == "__main__":
    alpha = float(input("Введіть значення α (у радіанах): "))
    print("Результат обчислення z =", calc_z(alpha))

    A = float(input("Введіть розмір стипендії (грн): "))
    B = float(input("Введіть витрати на проживання (грн): "))
    print("Сума грошей, яку треба попросити в батьків:",
          round(student_module.need_money(A, B), 2), "грн")
