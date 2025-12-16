"""
Задание 15: Куча
Реализация бинарной мин-кучи:
- вставка
- извлечение минимума
- построение кучи из массива
Проверка корректности свойств кучи после каждой операции.
"""

class MinHeap:
    """Реализация бинарной мин-кучи."""
    
    def __init__(self):
        """Инициализация пустой кучи."""
        self.heap = []
    
    def insert(self, value):
        """Вставка элемента в кучу. Сложность: O(log n)."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
        self._verify_heap()
    
    def extract_min(self):
        """Извлечение минимального элемента. Сложность: O(log n)."""
        if not self.heap:
            return None
        
        # Сохраняем минимум (корень)
        min_val = self.heap[0]
        
        # Заменяем корень последним элементом
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Просеиваем вниз
        if self.heap:
            self._sift_down(0)
        
        self._verify_heap()
        return min_val
    
    def build_heap(self, array):
        """Построение кучи из массива. Сложность: O(n)."""
        self.heap = array[:]
        
        # Начинаем с последнего нелистового узла
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)
        
        self._verify_heap()
    
    def _sift_up(self, index):
        """Просеивание вверх."""
        while index > 0:
            parent = (index - 1) // 2
            
            # Свойство мин-кучи: родитель <= ребенок
            if self.heap[parent] <= self.heap[index]:
                break
            
            # Меняем местами
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
    
    def _sift_down(self, index):
        """Просеивание вниз."""
        size = len(self.heap)
        
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            
            # Находим наименьший среди текущего и его детей
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            # Если текущий уже наименьший - завершаем
            if smallest == index:
                break
            
            # Меняем местами
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
    
    def _verify_heap(self):
        """Проверка свойства мин-кучи."""
        for i in range(len(self.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < len(self.heap) and self.heap[i] > self.heap[left]:
                raise ValueError(f"Нарушение свойства кучи: heap[{i}]={self.heap[i]} > heap[{left}]={self.heap[left]}")
            
            if right < len(self.heap) and self.heap[i] > self.heap[right]:
                raise ValueError(f"Нарушение свойства кучи: heap[{i}]={self.heap[i]} > heap[{right}]={self.heap[right]}")
        
        return True
    
    def peek_min(self):
        """Возвращает минимальный элемент без удаления. O(1)."""
        return self.heap[0] if self.heap else None
    
    def __str__(self):
        """Строковое представление кучи."""
        return str(self.heap)


def demonstrate():
    """Демонстрация работы бинарной мин-кучи."""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ БИНАРНОЙ МИН-КУЧИ")
    print("=" * 50)
    
    heap = MinHeap()
    
    # 1. Последовательная вставка
    print("\n1. Последовательная вставка элементов:")
    elements = [5, 3, 8, 1, 9, 2]
    
    for elem in elements:
        heap.insert(elem)
        print(f"Вставка {elem}: {heap}")
    
    # 2. Извлечение минимумов
    print("\n2. Извлечение минимальных элементов:")
    for _ in range(3):
        min_val = heap.extract_min()
        print(f"Извлечен {min_val}: {heap}")
    
    # 3. Построение кучи из массива
    print("\n3. Построение кучи из массива:")
    array = [9, 5, 7, 2, 8, 1, 6]
    heap.build_heap(array)
    print(f"Исходный массив: {array}")
    print(f"Построенная куча: {heap}")
    
    # 4. Проверка свойства кучи
    print("\n4. Проверка свойства мин-кучи:")
    try:
        if heap._verify_heap():
            print(" Свойство кучи выполняется!")
    except ValueError as e:
        print(f" {e}")
    
    # 5. Сортировка с помощью кучи
    print("\n5. Сортировка извлечением минимумов:")
    sorted_array = []
    while heap.heap:
        sorted_array.append(heap.extract_min())
    print(f"Отсортированный массив: {sorted_array}")
    
    print("\n" + "=" * 50)
    print("СВОЙСТВА И СЛОЖНОСТЬ:")
    print("  • Вставка: O(log n)")
    print("  • Извлечение минимума: O(log n)")
    print("  • Построение из массива: O(n)")
    print("  • Просмотр минимума: O(1)")
    print("  • Свойство кучи: родитель <= дети")
    print("\nПРИМЕНЕНИЕ:")
    print("  • Приоритетные очереди")
    print("  • Алгоритм Дейкстры")
    print("  • Пирамидальная сортировка")


if __name__ == "__main__":
    demonstrate()