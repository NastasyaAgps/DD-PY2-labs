class ElectronicDevice:
    """Базовый класс для представления электронных устройств."""

    def __init__(self, manufacturer: str, model: str, battery_level: int, serial_number: str) -> None:
        """
        Args:
            manufacturer: Производитель устройства
            model: Модель устройства
            battery_level: Начальный уровень заряда батареи (0-100%)
            serial_number: Уникальный серийный номер (приватный атрибут)
        """
        self.manufacturer = manufacturer
        self.model = model
        self.battery_level = battery_level
        self._serial_number = serial_number  # Инкапсуляция: защита от изменений

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model} [ {self.battery_level}%]"

    def __repr__(self) -> str:
        return (f"ElectronicDevice(manufacturer='{self.manufacturer}', "
                f"model='{self.model}', battery_level={self.battery_level}, "
                f"serial_number='{self._serial_number}')")

    def charge(self, percent: int) -> None:
        """Заряжает устройство на указанный процент."""
        self.battery_level = min(100, self.battery_level + percent)

    def check_battery(self) -> str:
        """Возвращает текстовый статус уровня заряда."""
        return f"Уровень заряда: {self.battery_level}%"


def make_call(number: str) -> str:
    """Совершает звонок на указанный номер."""
    return f"Набираем {number}..."


class Smartphone(ElectronicDevice):
    """Дочерний класс для представления смартфонов."""

    def __init__(self, manufacturer: str, model: str, battery_level: int,
                 serial_number: str, screen_size: float) -> None:
        super().__init__(manufacturer, model, battery_level, serial_number)
        self.screen_size = screen_size

    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info}  {self.screen_size}\""

    def __repr__(self) -> str:
        return (f"Smartphone(manufacturer='{self.manufacturer}', "
                f"model='{self.model}', battery_level={self.battery_level}, "
                f"serial_number='{self._serial_number}', screen_size={self.screen_size})")

    def check_battery(self) -> str:
        """
        Перегрузка метода с добавлением предупреждения.
        Обоснование: смартфоны требуют более частой подзарядки.
        """
        status = super().check_battery()
        if self.battery_level < 15:
            return f"{status}  Низкий заряд!"
        return status


class Laptop(ElectronicDevice):
    """Дочерний класс для представления ноутбуков."""

    def __init__(self, manufacturer: str, model: str, battery_level: int,
                 serial_number: str, ram_size: int) -> None:
        super().__init__(manufacturer, model, battery_level, serial_number)
        self.ram_size = ram_size

    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info}  {self.ram_size}GB RAM"

    def __repr__(self) -> str:
        return (f"Laptop(manufacturer='{self.manufacturer}', "
                f"model='{self.model}', battery_level={self.battery_level}, "
                f"serial_number='{self._serial_number}', ram_size={self.ram_size})")

    def check_battery(self) -> str:
        """
        Перегрузка метода с расчетом времени работы.
        Обоснование: для ноутбуков важна оценка времени автономной работы.
        """
        hours = round(self.battery_level * self.ram_size / 1000, 1)
        return f"{super().check_battery()} (~{hours}ч работы)"


if __name__ == "__main__":
    # Тестирование функционала
    phone = Smartphone("Xiaomi", "Redmi Note 10", 10, "XM123", 6.43)
    laptop = Laptop("Apple", "MacBook Pro", 75, "MBP456", 16)

    print(phone)  # Xiaomi Redmi Note 10 [ 10%]
    print(laptop)  # Apple MacBook Pro [ 75%]

    print(phone.check_battery())  # Уровень заряда: 10%  Низкий заряд!
    print(laptop.check_battery())  # Уровень заряда: 75% (~1.2ч работы)

    phone.charge(50)
    print(phone.check_battery())  # Уровень заряда: 60%
