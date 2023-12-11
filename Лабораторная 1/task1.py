import doctest


class University:
    def __init__(self, name: str, location: str, established_year: int):
        """
        Создание объекта "Университет"

        :param name: Название университета
        :param location: Местоположение университета
        :param established_year: Год основания университета

        Пример:
        >>> university = University("Example University", "Moscow", 2000)
        """
        if not isinstance(name, str):
            raise TypeError("Название университета должно быть строкой")
        self.name = name

        if not isinstance(location, str):
            raise TypeError("Местоположение университета должно быть строкой")
        self.location = location

        if not isinstance(established_year, int):
            raise TypeError("Год основания университета должен быть целым числом")
        self.established_year = established_year

    def enroll_student(self, student_name: str, major: str) -> None:
        """
        Зачисление студента в университет.

        :param student_name: Имя студента
        :param major: Направление подготовки

        Примеры:
        >>> university = University("Polytech", "St. Petersburg", 1985)
        >>> university.enroll_student("Polina", "Cybersecurity")
        """
        ...

    def conduct_research(self, topic: str) -> str:
        """
        Проведение исследования в университете.

        :param topic: Тема исследования
        :return: Результат исследования

        Примеры:
        >>> university = University("Example University", "Moscow", 2000)
        >>> university.conduct_research("Machine Learning")
        """
        ...


class Tree:
    def __init__(self, species: str, age: int, height: float):
        """
        Создание объекта "Дерево"

        :param species: Вид дерева
        :param age: Возраст дерева в годах
        :param height: Высота дерева в метрах

        Примеры:
        >>> tree = Tree("Oak", 10, 5.5)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        self.species = species

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        self.age = age

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числом")
        self.height = height

    def shed_leaves(self, season: str) -> None:
        """
        Осенью дерево сбрасывает листья.

        :param season: Время года (осень)

        Примеры:
        >>> tree = Tree("Maple", 8, 4.2)
        >>> tree.shed_leaves("autumn")
        """
        ...

    def grow(self, growth_rate: float) -> None:
        """
        Рост дерева.

        :param growth_rate: Скорость роста дерева

        Примеры:
        >>> tree = Tree("Pine", 5, 3.0)
        >>> tree.grow(0.5)
        """
        ...


class Cat:
    def __init__(self, name: str, age: int, color: str):
        """
        Создание объекта "Кошка"

        :param name: Имя кошки
        :param age: Возраст кошки в годах
        :param color: Цвет шерсти кошки

        Примеры:
        >>> cat = Cat("Barsik", 3, "White")
        """
        if not isinstance(name, str):
            raise TypeError("Имя кошки должно быть строкой")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст кошки должен быть целым числом")
        self.age = age

        if not isinstance(color, str):
            raise TypeError("Цвет шерсти кошки должен быть строкой")
        self.color = color

    def meow(self) -> None:
        """
        Издание "мяу".

        :return: Звук "мяу"

        Примеры:
        >>> cat = Cat("Sharik", 13, "Black")
        >>> cat.meow()
        """
        ...

    def sleep(self, hours: int) -> None:
        """
        Сон кошки.

        :param hours: Продолжительность сна в часах

        Примеры:
        >>> cat = Cat("Sonya", 4, "Orange")
        >>> cat.sleep(8)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
