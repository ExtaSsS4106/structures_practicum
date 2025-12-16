"""
Задание 6: Очередь
Реализация очереди на циклическом массиве.
Реализация очереди на двух стеках.
"""

# ===== Очередь на циклическом массиве =====
class CircularQueue:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def enqueue(self, value) -> None:
        """Добавление элемента в конец очереди."""
        if self.is_full():
            print(f" Очередь заполнена, расширяем до {self.capacity * 2}")
            self._resize(self.capacity * 2)
        
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
    
    def dequeue(self):
        """Удаление и возврат элемента из начала очереди."""
        if self.is_empty():
            raise Exception("Очередь пуста")
        
        value = self.data[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
    def peek(self):
        """Просмотр первого элемента без удаления."""
        if self.is_empty():
            raise Exception("Очередь пуста")
        return self.data[self.front]
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def is_full(self) -> bool:
        return self.size == self.capacity
    
    def get_size(self) -> int:
        return self.size
    
    def _resize(self, new_capacity: int) -> None:
        """Увеличение размера массива."""
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[(self.front + i) % self.capacity]
        
        self.data = new_data
        self.front = 0
        self.rear = self.size
        self.capacity = new_capacity
    
    def __str__(self) -> str:
        if self.is_empty():
            return "[]"
        
        elements = []
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            elements.append(str(self.data[idx]))
        
        return f"[{', '.join(elements)}] (size={self.size}, cap={self.capacity})"


# ===== Очередь на двух стеках =====
class QueueOnTwoStacks:
    def __init__(self):
        self.in_stack = []   # Для добавления
        self.out_stack = []  # Для удаления
    
    def enqueue(self, value) -> None:
        """Добавление элемента в конец очереди."""
        self.in_stack.append(value)
    
    def dequeue(self):
        """Удаление и возврат элемента из начала очереди."""
        if self.is_empty():
            raise Exception("Очередь пуста")
        
        if not self.out_stack:
            # Переносим все элементы из in_stack в out_stack
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack.pop()
    
    def peek(self):
        """Просмотр первого элемента без удаления."""
        if self.is_empty():
            raise Exception("Очередь пуста")
        
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack[-1]
    
    def is_empty(self) -> bool:
        return not self.in_stack and not self.out_stack
    
    def get_size(self) -> int:
        return len(self.in_stack) + len(self.out_stack)
    
    def __str__(self) -> str:
        # Собираем элементы в правильном порядке
        all_elements = []
        
        # Элементы из out_stack (в обратном порядке)
        for i in range(len(self.out_stack) - 1, -1, -1):
            all_elements.append(str(self.out_stack[i]))
        
        # Элементы из in_stack (в прямом порядке)
        all_elements.extend(map(str, self.in_stack))
        
        return f"[{', '.join(all_elements)}] (in={len(self.in_stack)}, out={len(self.out_stack)})"


# ===== Демонстрация работы =====
def demonstrate_queues():
    print("=" * 70)
    print("ДЕМОНСТРАЦИЯ РЕАЛИЗАЦИЙ ОЧЕРЕДИ")
    print("=" * 70)
    
    # Тестирование циклической очереди
    print("\n1. ОЧЕРЕДЬ НА ЦИКЛИЧЕСКОМ МАССИВЕ:")
    print("-" * 40)
    
    cq = CircularQueue(capacity=3)
    print(f"Создана очередь (емкость=3): {cq}")
    
    print("\nДобавление элементов:")
    for i in range(1, 5):
        cq.enqueue(i * 10)
        print(f"  enqueue({i*10}) -> {cq}")
    
    print("\nУдаление элементов:")
    for _ in range(2):
        val = cq.dequeue()
        print(f"  dequeue() = {val} -> {cq}")
    
    print(f"\nПросмотр первого элемента: peek() = {cq.peek()}")
    
    print("\nДобавление с циклическим поведением:")
    cq.enqueue(50)
    cq.enqueue(60)
    print(f"  enqueue(50), enqueue(60) -> {cq}")
    
    # Тестирование очереди на двух стеках
    print("\n\n2. ОЧЕРЕДЬ НА ДВУХ СТЕКАХ:")
    print("-" * 40)
    
    sq = QueueOnTwoStacks()
    print(f"Создана очередь: {sq}")
    
    print("\nДобавление элементов:")
    for i in range(1, 4):
        sq.enqueue(f"A{i}")
        print(f"  enqueue('A{i}') -> {sq}")
    
    print("\nУдаление элементов (с переносом между стеками):")
    for _ in range(2):
        val = sq.dequeue()
        print(f"  dequeue() = '{val}' -> {sq}")
    
    print("\nДобавление новых элементов после удаления:")
    sq.enqueue("B1")
    sq.enqueue("B2")
    print(f"  enqueue('B1'), enqueue('B2') -> {sq}")
    
    print("\nУдаление оставшихся элементов:")
    while not sq.is_empty():
        val = sq.dequeue()
        print(f"  dequeue() = '{val}' -> {sq}")
    
    # Сравнение
    print("\n\n3. СРАВНЕНИЕ РЕАЛИЗАЦИЙ:")
    print("-" * 40)
    print("Циклическая очередь:")
    print("  + Эффективное использование памяти")
    print("  + Постоянное время операций O(1)")
    print("  - Требует предварительного размера")
    print()
    print("Очередь на двух стеках:")
    print("  + Динамический размер")
    print("  + Простая реализация")
    print("  - Амортизированное O(1), иногда O(n)")
    print("  - Дополнительные затраты памяти")


# ===== Пример использования: система обработки заказов =====
def order_processing_example():
    print("\n\n" + "=" * 70)
    print("ПРИМЕР: СИСТЕМА ОБРАБОТКИ ЗАКАЗОВ")
    print("=" * 70)
    
    queue = CircularQueue(capacity=3)
    orders = ["Заказ #101", "Заказ #102", "Заказ #103", "Заказ #104", "Заказ #105"]
    
    print("Поступают заказы:")
    for order in orders:
        try:
            queue.enqueue(order)
            print(f"  {order} добавлен в очередь: {queue}")
        except:
            print(f"  Очередь переполнена! {order} ждет...")
    
    print("\nОбработка заказов:")
    while not queue.is_empty():
        order = queue.dequeue()
        print(f"  🔧 Обрабатывается {order}")
        print(f"    Осталось в очереди: {queue}")


# ===== Тестирование ошибок =====
def test_errors():
    print("\n\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ ГРАНИЧНЫХ СЛУЧАЕВ")
    print("=" * 70)
    
    print("1. Удаление из пустой очереди:")
    q = CircularQueue()
    try:
        q.dequeue()
    except Exception as e:
        print(f"  Ошибка: {e}")
    
    print("\n2. Просмотр пустой очереди:")
    try:
        q.peek()
    except Exception as e:
        print(f"  Ошибка: {e}")


# Главная функция
def main():
    demonstrate_queues()
    order_processing_example()
    test_errors()
    
    print("\n" + "=" * 70)
    print("ВЫВОДЫ:")
    print("1. Очередь - структура данных FIFO (First In, First Out)")
    print("2. Основные операции: enqueue (добавить), dequeue (удалить)")
    print("3. Циклическая очередь использует массив с круговыми индексами")
    print("4. Очередь на стеках использует два стека для эмуляции FIFO")
    print("=" * 70)


if __name__ == "__main__":
    main()