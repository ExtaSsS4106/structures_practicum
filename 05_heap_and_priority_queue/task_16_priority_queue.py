"""
Задание 16: Приоритетная очередь
Реализация на основе мин-кучи
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0  # Для сохранения порядка при одинаковых приоритетах
    
    def push(self, value, priority):
        """Добавляет элемент с приоритетом."""
        heapq.heappush(self.heap, (priority, self.counter, value))
        self.counter += 1
    
    def pop(self):
        """Извлекает элемент с минимальным приоритетом."""
        if not self.heap:
            return None
        _, _, value = heapq.heappop(self.heap)
        return value
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def __len__(self):
        return len(self.heap)


# Пример 1: Планирование задач
def task_scheduler():
    print("1. Планировщик задач:")
    pq = PriorityQueue()
    
    # Добавляем задачи с приоритетами (меньше = выше приоритет)
    tasks = [
        ("Отправка email", 3),
        ("Обработка платежа", 1),
        ("Резервное копирование", 5),
        ("Срочная задача", 0),
    ]
    
    for task, priority in tasks:
        pq.push(task, priority)
        print(f"  Добавлено: {task} (приоритет: {priority})")
    
    print("\n  Выполнение задач:")
    while not pq.is_empty():
        task = pq.pop()
        print(f"    Выполняется: {task}")


# Пример 2: Поиск k минимальных элементов
def find_k_smallest(arr, k):
    print(f"\n2. Поиск {k} минимальных элементов:")
    print(f"   Массив: {arr}")
    
    # Создаем макс-кучу (храним отрицательные значения)
    max_heap = []
    
    for i, num in enumerate(arr):
        if i < k:
            heapq.heappush(max_heap, -num)  # Отрицательное для макс-кучи
        elif num < -max_heap[0]:
            heapq.heapreplace(max_heap, -num)
    
    # Преобразуем результат
    result = sorted([-x for x in max_heap])
    print(f"   Результат: {result}")
    return result


# Демонстрация
def demonstrate():
    print("=" * 50)
    print("ПРИОРИТЕТНАЯ ОЧЕРЕДЬ")
    print("=" * 50)
    
    # 1. Планирование задач
    task_scheduler()
    
    # 2. Поиск k минимальных
    import random
    arr = [random.randint(1, 100) for _ in range(10)]
    find_k_smallest(arr, 4)
    
    print("\n" + "=" * 50)
    print("СЛОЖНОСТЬ:")
    print("  • push: O(log n)")
    print("  • pop: O(log n)")
    print("  • peek: O(1)")


if __name__ == "__main__":
    demonstrate()