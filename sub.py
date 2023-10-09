pi = 3.1415
def pramoygol():
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))

    rectangle_area = length * width
    rectangle_perimeter = 2 * (length + width)

    print("Площадь прямоугольника:", rectangle_area)
    print("Периметр прямоугольника:", rectangle_perimeter)


def cwadrat():
    side = float(input("Введите сторону квадрата: "))
    square_area = side ** 2
    square_perimeter = 4 * side
    print("Площадь квадрата:", square_area)
    print("Периметр квадрата:", square_perimeter)


def crug():
    radius = float(input("Введите радиус круга: "))


    circle_area = pi * radius ** 2
    circle_circumference = 2 * pi * radius

    print("Площадь круга:", circle_area)
    print("Длина окружности:", circle_circumference)


def treygol():
    base = float(input("Введите длину основания треугольника: "))
    height = float(input("Введите высоту треугольника: "))

    triangle_area = 0.5 * base * height
    triangle_perimeter = base + 2 * height  # предполагаем, что это периметр

    print("Площадь треугольника:", triangle_area)
    print("Периметр треугольника:", triangle_perimeter)


def pram_treygol():
    base = float(input("Введите длину основания прямоугольного треугольника: "))
    height = float(input("Введите высоту прямогоугольного треугольника: "))

    right_triangle_area = 0.5 * base * height  # площадь
    right_triangle_perimeter = base + height + (base ** 2 + height ** 2) ** 0.5  # периметр

    print("Площадь прямоугольного треугольника:", right_triangle_area)
    print("Периметр прямоугольного треугольника:", right_triangle_perimeter)


# ФОРМУЛЫ РАСЧЕТА ОБЪЕМА И ПЛОЩАДИ ДЛЯ ТРЕХМЕРНЫХ ФИГУР

def paralelepiped():
    length = float(input("Введите длину параллелепипеда: "))
    width = float(input("Введите ширину параллелепипеда: "))
    height = float(input("Введите высоту параллелепипеда: "))

    cuboid_volume = length * width * height
    cuboid_surface_area = 2 * (length * width + length * height + width * height)

    print("Объем прямоугольного параллелепипеда:", cuboid_volume)
    print("Площадь поверхности прямоугольного параллелепипеда:", cuboid_surface_area)


def kub():
    side = float(input("Введите длину стороны куба: "))

    cube_volume = side ** 3
    cube_surface_area = 6 * side ** 2

    print("Объем куба:", cube_volume)
    print("Площадь поверхности куба:", cube_surface_area)


def shar():
    radius = float(input("Введите радиус шара: "))

    sphere_volume = 4 / 3 * pi * radius ** 3
    sphere_surface_area = 4 * pi * radius ** 2

    print("Объем шара:", sphere_volume)
    print("Площадь поверхности шара:", sphere_surface_area)


def conuc():
    radius = float(input("Введите радиус основания конуса: "))
    height = float(input("Введите высоту конуса: "))

    cone_volume = 1 / 3 * pi * radius ** 2 * height
    cone_surface_area = pi * radius * (radius + (radius ** 2 + height ** 2) ** 0.5)

    print("Объем конуса:", cone_volume)
    print("Площадь поверхности конуса:", cone_surface_area)


if __name__ == "__main__":
    print(f"Выберите желаемую фигуру\n "
          f"1. Прямоугольник\n"
          "2. Квадрат\n"
          "3. Круг\n"
          "4. Треугольник\n"
          "5. Прямоугольный треугольник\n"
          "Трехмерные фигуры:\n"
          "6. Прямоугольный параллелепипед\n"
          "7. Куб\n"
          "8. Шар\n"
          "9. Конус")

    while True:
        command = input()
        match command:
            case "1":
                pramoygol()
            case "2":
                cwadrat()
            case "3":
                crug()
            case "4":
                treygol()
            case "5":
                pram_treygol()
            case "6":
                paralelepiped()
            case "7":
                kub()
            case "8":
                shar()
            case "9":
                conuc()
