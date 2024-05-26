import random
import math
import numpy
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def normally_distributed_nums(n):
    nums = []
    for x in range(0, n):
        nums.append(numpy.random.normal(0.0, 1.0))
    return nums
# הגרלת ערכיים אקראיים בהסתברות נורמלית


def get_point_on_unit_hypersphere(n):
    nums = normally_distributed_nums(n)
    sos = 0.0
    # sos=sum of square
    for x in nums:
        sos += x * x
    sos = math.sqrt(sos)
    for x in nums:
        x /= sos
    return nums
# הפיכת הערכים שיתאימו לווקטור יחידה (לחלק בשורש סכום הריבועים)


def get_coang(n):
    nums = get_point_on_unit_hypersphere(n)
    sos = nums[n - 1] ** 2
    for x in range(n-2, -1, -1):
        sos += nums[x] ** 2
    sqrtsos = math.sqrt(sos)
    coang = nums[x] / sqrtsos
    return coang
# מציאת קוסינוס זווית הווקטור


def finding_growth_in_nth_dimension_1st_way(n):
    a = 1.0
    b = 1.0
    for i in range(1, 500000):
        print(f'{abs(a) ** (1 / i)}')
        # הדפסת שורש nי
        temp = b * get_coang(n)
        # יצירת ההיטל של האיבר על ציר הx
        c = a + temp
        a = b
        b = c
# יצירת הסדרה a


def finding_growth_in_nth_dimension_2nd_way(n):
    a = 1.0
    b = 1.0
    for i in range(1, 500000):
        print(f'{abs(a) ** (1 / i)}')
        # הדפסת שורש nי
        coang = get_coang(n)
        c = math.sqrt(a**2 + b**2 - 2 * a * b * coang)
        # חיבור הווקטורים
        a = b
        b = c
# יצירת הסדרה b


def using_k(k, n):
    a = 1.0
    b = 1.0
    for i in range(1, 100000):
        print(f'{abs(a) ** (1 / i)}')
        # הדפסת שורש nי
        coang = get_coang(n)
        c = math.sqrt(a**2 + (k*b)**2 - 2 * a * k * b * coang)
        # חיבור הווקטורים
        a = b
        b = c
# יצירת הסדרה b עם קבוע k


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    finding_growth_in_nth_dimension_1st_way(1000)
    finding_growth_in_nth_dimension_2nd_way(1000)
    using_k(1/100, 2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
