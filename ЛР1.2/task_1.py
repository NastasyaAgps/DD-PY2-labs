import doctest

class Apple:
    def __init__(self, size_apple: float, color_apple: str):
        """
        Создание и подготовка к работе объекта "Яблоко"
        :param size_apple: Размер яблока
        :param color_apple: Цвет яблока

        Примеры:
        >>> apple = Apple(25, "Зелёный")  # инициализация экземпляра класса
        """
        if not isinstance(size_apple, (int, float)):
            raise TypeError("Размер яблока должен быть типа int или float")
        if size_apple <= 0:
            raise ValueError("Размер яблока должен быть положительным числом")
        self.size_apple = size_apple

        if not isinstance(color_apple, str):
            raise TypeError("Цвет яблока должен быть типа str")
        if color_apple.lower()!=("зелёный" or "красный" or "жёлтый"):
            raise ValueError("Цвет яблока должен быть естественным")
        self.color_apple = color_apple

    def cut_part_of_apple(self, size_part: (int, float)) -> None:
        """
        Уменьшение размера яблока.

        :param : size_part: Размер отрезанной части
        :raise ValueError: Если отрезанная часть превышает размер яблока, то возвращается ошибка.

         Примеры:
         >>> apple = Apple(25,"зелёный")
         >>> apple.cut_part_of_apple(20)
         """
    ...

     def add_size_for_apple(self, size: (int, float)) -> None:
         """Добавление части к яблоку.
            :param size: Размер добавленной части
            :raise TypeError: Если указывается неправильный тип данных, то вызываем ошибку

            Примеры:
            >>> apple = Apple(25, "зелёный")
            >>> apple.add_size_for_apple(200)
            """
     ...

    def check_color_green(self) -> bool:
    """
    Функция которая проверяет является ли яблоко зеленым

    :return: Является ли яблоко зеленым

    Примеры:
    >>>  apple= Apple (25, "зелёный")
    >>> apple.check_color_green()
    """
    ...

class Car:
    def __init__(self, plus: bool, quanty: int):
        """
          Создание и подготовка к работе объекта "Машина"

        :param plus: Наличие прицепа
        :param quanty: Количество пассажиров

        Примеры:
        >>> car = Car(true , 5)  # инициализация экземпляра класса
                        """
        if not isinstance(plus, bool):
             raise TypeError("Тип данных должен быть типа bool")
        self.plus = plus
        if (quanty<= 0) and (quanty>= 6):
            raise ValueError("Количество пассажиров должно быть не более 6 человек и не менее 0")
        if not isinstance(quanty, int):
            raise TypeError("Количество пассажиров должно быть типа int ")
        self.quanty = quanty

    def conditions (self) -> bool:
        """
        Проверка условий (Машина с прицепом и с минимальным количеством пассажиров 5)
        :return Условия выполняются
         Примеры:
         >>> car = Car(true,5)
         >>> car.conditions()
         """
        ...
    def people_delete(self, quanty: int) -> None:
        """
        Уменьшение количества пассажиров.

        :param : quanty: Количество вычитаемых пассажиров
        :raise ValueError: Если количество вычитаемых пассажиров превышает количество пассажиров в машине , то возвращается ошибка.

         Примеры:
         >>> car = Car(true,5)
         >>> car.people_delete(4)
         """
        ...
class Flowers:
    def __init__(self, smell: str, color: str):
        """
            Создание и подготовка к работе объекта "Цветы"

            :param smell: Запах цветов
            :param color: Цвет цветов

            Примеры:
            >>> flowers = Flowers("sweet", "pink")  # инициализация экземпляра класса
            """
        if not isinstance(color, str):
            raise TypeError("Цвет цветов должен быть типа str")
        if color.lower() == ("grey"):
            raise ValueError("Цвет цветов должен быть естественным")
        self.color = color
        if not isinstance(smell, str):
            raise TypeError("Запах цветов должен быть типа str")
        if smell.lower() == ("terrible"):
            raise ValueError("Запах цветов должен быть приятным")
        self.smell= smell
    def check_smell_nice(self) -> bool:
            """
            Функция которая проверяет приятный ли запах у цветов

            :return: Является ли запах приятным

            Примеры:
            >>>  flowers= Flowers ("nice", "red")
            >>> flowers.check_smell_nice()
            """
            ...
    def found_great(self) -> bool:
        """
        Проверка условий (Цветы должны иметь пурпурный цвет и иметь сладкий аромат)
        :return Условия выполняются
         Примеры:
                 >>> flowers = Flowers("sweet","purpure")
                 >>> flowers.found_great()
                 """
        ...
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации