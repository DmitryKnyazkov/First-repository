# TODO Вынести константу pi
P = 3.14

# TODO убрать аргумент pi из функций и заменить его на константу из глобальной области видимости
def square_circle(r):
    return P * r ** 2


def length_circle(r):
    return 2 * P * r


radius = 8  # радиус круга
# TODO подправить передаваемые аргументы
square = square_circle(radius)
length = length_circle(radius)

print("Площадь равна =", square)
print("Длина окружности равна =", length)
