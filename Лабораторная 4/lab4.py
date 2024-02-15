class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Конструктор класса Vehicle.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        """
        Метод запуска двигателя.
        """
        pass

    def stop_engine(self):
        """
        Метод остановки двигателя.
        """
        pass

    def __str__(self) -> str:
        """
        Магический метод преобразования в строку.
        """
        return f"{self.year} {self.brand} {self.model}"

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки.
        """
        return f"Vehicle(brand={self.brand}, model={self.model}, year={self.year})"


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        """
        Конструктор класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param num_doors: Количество дверей у автомобиля.
        """
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def start_engine(self):
        """
        Перегруженный метод запуска двигателя для автомобиля.
        Добавляет специфичное поведение для автомобиля.
        """
        pass

    def open_trunk(self):
        """
        Метод открытия багажника автомобиля.

        :return: Состояние багажника (открыт/закрыт).
        :rtype: bool
        """
        pass

    def __str__(self) -> str:
        """
        Перегруженный магический метод преобразования в строку для автомобиля.
        Добавляет информацию о количестве дверей.
        """
        return f"{super().__str__()}, {self.num_doors}-door"


    def __repr__(self) -> str:
        """
        Перегруженный магический метод для представления объекта в виде строки для автомобиля.
        """
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, num_doors={self.num_doors})"
