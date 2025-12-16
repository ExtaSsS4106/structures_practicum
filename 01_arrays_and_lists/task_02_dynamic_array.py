"""
Задание 2: Динамический массив
Реализация динамического массива с автоматическим расширением (стратегия ×2).
Сравнение времени вставки 100000 элементов со статическим массивом.
"""

import time
import sys

class DynamicArray:
    """Динамический массив с автоматическим расширением."""
    
    def __init__(self, initial_capacity: int = 4):
        """Инициализация динамического массива.
        
        Args:
            initial_capacity: Начальная емкость массива
        """
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * initial_capacity
        self.expansions = 0  # Счетчик расширений
    
    def append(self, value) -> None:
        """Добавление элемента в конец массива.
        
        Амортизированная сложность: O(1)
        В худшем случае (при расширении): O(n)
        """
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)  # Стратегия увеличения ×2
        
        self.data[self.size] = value
        self.size += 1
    
    def _resize(self, new_capacity: int) -> None:
        """Внутренний метод для изменения размера массива.
        
        Сложность: O(n) - копирование всех элементов.
        """
        self.expansions += 1
        print(f"  Расширение массива: {self.capacity} → {new_capacity}")
        
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.data = new_data
        self.capacity = new_capacity
    
    def get(self, index: int):
        """Получение элемента по индексу.
        
        Сложность: O(1)
        """
        if index < 0 or index >= self.size:
            raise IndexError(f"Индекс {index} вне диапазона [0, {self.size-1}]")
        return self.data[index]
    
    def __str__(self) -> str:
        """Строковое представление массива."""
        elements = [str(self.data[i]) for i in range(self.size)]
        return f"[{', '.join(elements)}] (size={self.size}, capacity={self.capacity})"
    
    def get_stats(self) -> dict:
        """Возвращает статистику по массиву."""
        return {
            "size": self.size,
            "capacity": self.capacity,
            "expansions": self.expansions,
            "load_factor": self.size / self.capacity if self.capacity > 0 else 0,
            "memory_usage": sys.getsizeof(self.data) + sys.getsizeof(self)  # Байты
        }


# ===== Статический массив для сравнения =====
class StaticArrayForComparison:
    """Упрощенный статический массив для сравнения производительности."""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def append(self, value) -> None:
        if self.size >= self.capacity:
            raise Exception("Массив переполнен!")
        self.data[self.size] = value
        self.size += 1


# ===== Демонстрация работы динамического массива =====
def demonstrate_dynamic_array():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ДИНАМИЧЕСКОГО МАССИВА")
    print("=" * 60)
    
    # Создаем динамический массив с маленькой начальной емкостью
    dyn_arr = DynamicArray(initial_capacity=2)
    print(f"Создан динамический массив с начальной емкостью: {dyn_arr.capacity}")
    print()
    
    # Добавляем элементы и наблюдаем за расширением
    print("1. Добавление элементов с автоматическим расширением:")
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    for i, value in enumerate(values, 1):
        print(f"  Шаг {i}: Добавляю {value}")
        dyn_arr.append(value)
        print(f"    Состояние: {dyn_arr}")
        print(f"    Статистика: размер={dyn_arr.size}, емкость={dyn_arr.capacity}")
    print()
    
    # Показываем конечную статистику
    print("2. Итоговая статистика:")
    stats = dyn_arr.get_stats()
    for key, value in stats.items():
        print(f"  {key:15}: {value}")
    print()
    
    # Доступ к элементам
    print("3. Доступ к элементам по индексу:")
    for i in [0, 3, 7, 9]:
        print(f"  arr[{i}] = {dyn_arr.get(i)}")
    print()


# ===== Сравнение производительности =====
def compare_performance():
    print("=" * 60)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 60)
    
    n_elements = 100000
    
    # Тестируем динамический массив
    print("1. Тест динамического массива (100000 элементов):")
    dyn_arr = DynamicArray(initial_capacity=4)
    
    start_time = time.time()
    for i in range(n_elements):
        dyn_arr.append(i)
    dyn_time = time.time() - start_time
    
    dyn_stats = dyn_arr.get_stats()
    print(f"  Время: {dyn_time:.4f} секунд")
    print(f"  Расширений: {dyn_stats['expansions']}")
    print(f"  Финальная емкость: {dyn_stats['capacity']}")
    print(f"  Коэффициент загрузки: {dyn_stats['load_factor']:.2%}")
    print()
    
    # Тестируем статический массив
    print("2. Тест статического массива (100000 элементов):")
    
    # Пытаемся использовать статический массив
    try:
        static_arr = StaticArrayForComparison(capacity=n_elements)
        
        start_time = time.time()
        for i in range(n_elements):
            static_arr.append(i)
        static_time = time.time() - start_time
        
        print(f"  Время: {static_time:.4f} секунд")
        print(f"  Размер: {static_arr.size}, Емкость: {static_arr.capacity}")
        
    except Exception as e:
        print(f"  Ошибка: {e}")
        print("  Статический массив требует заранее известной емкости!")
        print()
        
        # Альтернатива: статический массив с меньшей емкостью
        print("3. Тест статического массива с недостаточной емкостью:")
        small_static = StaticArrayForComparison(capacity=100)
        
        start_time = time.time()
        try:
            for i in range(n_elements):
                small_static.append(i)
        except Exception as e:
            static_time = time.time() - start_time
            print(f"  Время до ошибки: {static_time:.4f} секунд")
            print(f"  Успешно добавлено: {small_static.size} элементов")
    
    print()
    
    # Сравнение амортизированной сложности
    print("4. Анализ амортизированной сложности:")
    print("  Динамический массив:")
    print("    - Одна операция append: O(1) в среднем (амортизированно)")
    print("    - Расширение массива: O(n), но происходит редко")
    print("    - Итог: n операций append = O(n) амортизированно")
    print()
    print("  Статический массив:")
    print("    - Одна операция append: O(1)")
    print("    - Но требуется знать размер заранее")
    print("    - Или рисковать переполнением")


# ===== Визуализация процесса расширения =====
def visualize_expansion():
    print("\n" + "=" * 60)
    print("ВИЗУАЛИЗАЦИЯ ПРОЦЕССА РАСШИРЕНИЯ")
    print("=" * 60)
    
    # Создаем массив с очень маленькой начальной емкостью
    arr = DynamicArray(initial_capacity=1)
    print(f"Начальная емкость: {arr.capacity}")
    print()
    
    # Добавляем элементы и фиксируем изменения
    expansions_log = []
    
    for i in range(10):
        old_capacity = arr.capacity
        arr.append(i)
        new_capacity = arr.capacity
        
        if old_capacity != new_capacity:
            expansions_log.append({
                "element": i,
                "old_capacity": old_capacity,
                "new_capacity": new_capacity,
                "size": arr.size
            })
    
    print("Журнал расширений:")
    for log in expansions_log:
        print(f"  При добавлении {log['element']}:")
        print(f"    Размер: {log['size']-1} → {log['size']}")
        print(f"    Емкость: {log['old_capacity']} → {log['new_capacity']}")
        print(f"    Увеличение в {log['new_capacity'] / log['old_capacity']} раз")
        print()


# Запуск демонстрации
if __name__ == "__main__":
    demonstrate_dynamic_array()
    compare_performance()
    visualize_expansion()
    
    print("=" * 60)
    print("ВЫВОДЫ:")
    print("  1. Динамический массив автоматически расширяется при необходимости")
    print("  2. Стратегия увеличения ×2 обеспечивает амортизированную O(1)")
    print("  3. Статический массив быстрее, но требует знания размера заранее")
    print("  4. Динамический массив более гибкий, но имеет накладные расходы")
    print("  5. Выбор зависит от задачи: если размер известен - статический,")
    print("     если нет - динамический")
    print("=" * 60)