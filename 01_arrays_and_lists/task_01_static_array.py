"""
Задание 1: Статический массив
Реализация статического массива с фиксированной емкостью и основными операциями.
Оценим трудоемкость каждой операции.
"""

class StaticArray:
    def __init__(self, capacity: int):
        """Инициализация статического массива с заданной емкостью.
        
        Args:
            capacity: Максимальное количество элементов
        """
        self.capacity = capacity
        self.size = 0  # Текущее количество элементов
        self.data = [None] * capacity
    
    def pushBack(self, value) -> None:
        """Добавление элемента в конец массива.
        
        Сложность: O(1) - просто запись по индексу.
        """
        if self.size >= self.capacity:
            raise Exception(f"Массив переполнен! Емкость: {self.capacity}")
        self.data[self.size] = value
        self.size += 1
    
    def pushFront(self, value) -> None:
        """Добавление элемента в начало массива.
        
        Сложность: O(n) - нужно сдвинуть все существующие элементы.
        """
        if self.size >= self.capacity:
            raise Exception(f"Массив переполнен! Емкость: {self.capacity}")
        
        # Сдвигаем все элементы вправо
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i-1]
        
        self.data[0] = value
        self.size += 1
    
    def insert(self, index: int, value) -> None:
        """Вставка элемента по указанному индексу.
        
        Сложность: O(n) - в худшем случае сдвиг n элементов.
        """
        if self.size >= self.capacity:
            raise Exception(f"Массив переполнен! Емкость: {self.capacity}")
        if index < 0 or index > self.size:
            raise IndexError(f"Индекс {index} вне диапазона [0, {self.size}]")
        
        # Сдвигаем элементы от конца до индекса
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        
        self.data[index] = value
        self.size += 1
    
    def remove(self, index: int) -> None:
        """Удаление элемента по указанному индексу.
        
        Сложность: O(n) - сдвиг элементов влево.
        """
        if index < 0 or index >= self.size:
            raise IndexError(f"Индекс {index} вне диапазона [0, {self.size-1}]")
        
        # Сдвигаем элементы влево, начиная с индекса
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.size -= 1
        self.data[self.size] = None  # Очищаем последний элемент
    
    def find(self, value) -> int:
        """Поиск элемента по значению.
        
        Сложность: O(n) - линейный поиск.
        
        Returns:
            Индекс первого найденного элемента или -1 если не найден.
        """
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def __str__(self) -> str:
        """Строковое представление массива."""
        return f"[{', '.join(str(self.data[i]) for i in range(self.size))}]"
    
    def get_capacity(self) -> int:
        """Возвращает емкость массива."""
        return self.capacity
    
    def get_size(self) -> int:
        """Возвращает текущий размер массива."""
        return self.size


# ===== Демонстрация работы статического массива =====
def demonstrate_static_array():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ СТАТИЧЕСКОГО МАССИВА")
    print("=" * 60)
    
    # Создаем статический массив емкостью 10
    arr = StaticArray(10)
    print(f"Создан массив. Емкость: {arr.get_capacity()}, Размер: {arr.get_size()}")
    print(f"Массив: {arr}")
    print()
    
    # Добавляем элементы в конец
    print("1. Добавление элементов в конец (pushBack):")
    for i in range(1, 6):
        arr.pushBack(i * 10)
        print(f"  Добавил {i*10}: {arr}")
    print()
    
    # Добавляем элемент в начало
    print("2. Добавление элемента в начало (pushFront):")
    arr.pushFront(999)
    print(f"  Добавил 999 в начало: {arr}")
    print()
    
    # Вставляем элемент по индексу
    print("3. Вставка элемента по индексу 2 (insert):")
    arr.insert(2, 777)
    print(f"  Вставил 777 по индексу 2: {arr}")
    print()
    
    # Ищем элементы
    print("4. Поиск элементов (find):")
    values_to_find = [777, 30, 999, 1000]
    for value in values_to_find:
        index = arr.find(value)
        if index != -1:
            print(f"  Значение {value} найдено по индексу {index}")
        else:
            print(f"  Значение {value} не найдено")
    print()
    
    # Удаляем элементы
    print("5. Удаление элементов (remove):")
    print(f"  Удаляю элемент по индексу 3 (значение: {arr.data[3]}):")
    arr.remove(3)
    print(f"  Результат: {arr}")
    
    print(f"  Удаляю элемент по индексу 0 (первый элемент):")
    arr.remove(0)
    print(f"  Результат: {arr}")
    print()
    
    # Пытаемся превысить емкость
    print("6. Попытка превысить емкость массива:")
    try:
        print("  Пытаюсь добавить еще 6 элементов...")
        for i in range(6):
            arr.pushBack((i + 10) * 10)
    except Exception as e:
        print(f"  Ошибка: {e}")
        print(f"  Текущее состояние: {arr}")
        print(f"  Размер: {arr.get_size()}, Емкость: {arr.get_capacity()}")
    print()
    
    # Итоговая информация
    print("7. Итоговая информация:")
    print(f"  Массив: {arr}")
    print(f"  Размер: {arr.get_size()}")
    print(f"  Емкость: {arr.get_capacity()}")
    print(f"  Свободное место: {arr.get_capacity() - arr.get_size()}")
    
    print("\n" + "=" * 60)
    print("ВЫВОД:")
    print("  - pushBack: O(1) - быстрое добавление в конец")
    print("  - pushFront: O(n) - медленное из-за сдвига всех элементов")
    print("  - insert: O(n) - зависит от позиции вставки")
    print("  - remove: O(n) - зависит от позиции удаления")
    print("  - find: O(n) - линейный поиск")
    print("  - Главный недостаток: фиксированный размер")
    print("=" * 60)


# ===== Анализ сложности операций =====
def complexity_analysis():
    print("\n" + "=" * 60)
    print("АНАЛИЗ СЛОЖНОСТИ ОПЕРАЦИЙ СТАТИЧЕСКОГО МАССИВА")
    print("=" * 60)
    
    complexities = {
        "pushBack": "O(1) - прямое присвоение по индексу",
        "pushFront": "O(n) - сдвиг всех элементов вправо",
        "insert": "O(n) - в худшем случае сдвиг n элементов",
        "remove": "O(n) - сдвиг элементов для заполнения 'дырки'",
        "find": "O(n) - последовательный перебор элементов",
        "доступ по индексу": "O(1) - прямое обращение по адресу",
    }
    
    for operation, complexity in complexities.items():
        print(f"  {operation:20} → {complexity}")


# Запуск демонстрации
if __name__ == "__main__":
    demonstrate_static_array()
    complexity_analysis()