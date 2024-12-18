from abc import ABC, abstractmethod


class Table(ABC):
    """
    Класс, описывающий стол.

    Атрибуты:
        material (str): Материал, из которого изготовлен стол.
        height (float): Высота стола в сантиметрах.
        width (float): Ширина стола в сантиметрах.

    Методы:
        adjust_height(new_height: float) -> None: Изменяет высоту стола.
        describe() -> str: Возвращает описание стола.
    """

    def __init__(self, material: str, height: float, width: float) -> None:
        if height <= 0:
            raise ValueError("Высота стола должна быть положительным числом.")
        if width <= 0:
            raise ValueError("Ширина стола должна быть положительным числом.")

        self.material = material
        self.height = height
        self.width = width

    @abstractmethod
    def adjust_height(self, new_height: float) -> None:
        """
        Изменяет высоту стола.

        :param new_height: Новая высота стола.
        :raises ValueError: Если новая высота не положительна.

        >>> table = Table("Дерево", 75, 120)
        >>> table.adjust_height(80)
        >>> table.height
        80
        """
        ...

    @abstractmethod
    def describe(self) -> str:
        """
        Возвращает описание стола.

        :return: Описание стола.

        >>> table = Table("Дерево", 75, 120)
        >>> table.describe()
        'Стол из дерева, высота 75 см и ширина 120 см.'
        """
        ...


class Tree(ABC):
    """
    Класс, описывающий дерево.

    Атрибуты:
        species (str): Вид дерева.
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.

    Методы:
        grow(years: int) -> None: Увеличивает высоту дерева.
        describe() -> str: Возвращает описание дерева.
    """

    def __init__(self, species: str, height: float, age: int) -> None:
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.species = species
        self.height = height
        self.age = age

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличивает высоту дерева.

        :param years: Количество лет, на которое нужно увеличить высоту.
        :raises ValueError: Если количество лет не положительно.

        >>> tree = Tree("Дуб", 5, 10)
        >>> tree.grow(2)
        >>> tree.height
        7
        """
        ...

    @abstractmethod
    def describe(self) -> str:
        """
        Возвращает описание дерева.

        :return: Описание дерева.

        >>> tree = Tree("Дуб", 5, 10)
        >>> tree.describe()
        'Дерево вида Дуб, высота 5 м и возраст 10 лет.'
        """
        ...


class Stack(ABC):
    """
    Класс, описывающий стек.

    Атрибуты:
        items (list): Элементы стека.

    Методы:
        push(item: Any) -> None: Добавляет элемент на верх стека.
        pop() -> Any: Удаляет верхний элемент стека и возвращает его.
    """

    def __init__(self) -> None:
        self.items = []

    @abstractmethod
    def push(self, item: any) -> None:
        """
        Добавляет элемент на верх стека.

        :param item: Элемент, который нужно добавить в стек.

        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.items
        [1]
        """
        ...

    @abstractmethod
    def pop(self) -> any:
        """
        Удаляет верхний элемент стека и возвращает его.

        :return: Верхний элемент стека.
        :raises IndexError: Если стек пуст.

        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
