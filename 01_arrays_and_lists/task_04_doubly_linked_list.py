"""
Задание 4: Двусвязный список
Реализовать:
- вставку после произвольного узла,
- удаление узла без поиска "сначала".
Реализовать итератор по двусвязному списку.
"""

class DoublyNode:
    """Узел двусвязного списка."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """Двусвязный список."""
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_after(self, node: DoublyNode, value) -> DoublyNode:
        """Вставка после произвольного узла. Сложность: O(1)"""
        if node is None:
            raise ValueError("Узел не может быть None")
        
        new_node = DoublyNode(value)
        
        # Настраиваем связи нового узла
        new_node.prev = node
        new_node.next = node.next
        
        # Обновляем связи соседних узлов
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        
        # Если вставляли после хвоста, обновляем tail
        if node == self.tail:
            self.tail = new_node
        
        return new_node
    
    def delete_node(self, node: DoublyNode) -> None:
        """Удаление узла без поиска. Сложность: O(1)"""
        if node is None:
            return
        
        # Обновляем связи соседних узлов
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        # Обновляем head и tail при необходимости
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
    
    # Вспомогательные методы для демонстрации
    def append(self, value) -> DoublyNode:
        """Добавление в конец (для создания списка)."""
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node
    
    def __str__(self) -> str:
        """Строковое представление списка."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " ↔ ".join(elements) if elements else "Пусто"
    
    # Итератор
    class DoublyLinkedListIterator:
        def __init__(self, start_node, reverse=False):
            self.current = start_node
            self.reverse = reverse
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current is None:
                raise StopIteration
            
            value = self.current.value
            if self.reverse:
                self.current = self.current.prev
            else:
                self.current = self.current.next
            
            return value
    
    def __iter__(self):
        """Итерация в прямом порядке."""
        return self.DoublyLinkedListIterator(self.head)
    
    def reverse_iterator(self):
        """Итерация в обратном порядке."""
        return self.DoublyLinkedListIterator(self.tail, reverse=True)


# Демонстрация работы
if __name__ == "__main__":
    print("=== Демонстрация двусвязного списка ===\n")
    
    # Создание списка
    dll = DoublyLinkedList()
    print("1. Создаем список [1, 2, 3]:")
    node1 = dll.append(1)
    node2 = dll.append(2)
    node3 = dll.append(3)
    print(f"   Список: {dll}")
    
    print("\n2. Вставка после узла со значением 2:")
    dll.insert_after(node2, 99)
    print(f"   Список: {dll}")
    
    print("\n3. Вставка после хвоста (значение 3):")
    dll.insert_after(node3, 100)
    print(f"   Список: {dll}")
    
    print("\n4. Удаление узла со значением 2 (без поиска):")
    dll.delete_node(node2)
    print(f"   Список: {dll}")
    
    print("\n5. Удаление головы (значение 1):")
    dll.delete_node(node1)
    print(f"   Список: {dll}")
    
    print("\n6. Итерация по списку:")
    print("   Прямой порядок:", end=" ")
    for value in dll:
        print(value, end=" ")
    
    print("\n   Обратный порядок:", end=" ")
    for value in dll.reverse_iterator():
        print(value, end=" ")
    
    print("\n\n7. Сравнение с односвязным списком:")
    print("   Двусвязный список:")
    print("     - Удаление узла: O(1) (узел уже известен)")
    print("     - Вставка после узла: O(1)")
    print("     - Итерация в обе стороны: поддерживается")
    print("     - Память: 2 указателя на узел (prev, next)")
    
    print("\n   Односвязный список:")
    print("     - Удаление узла: O(n) (нужно найти предыдущий)")
    print("     - Вставка после узла: O(1)")
    print("     - Итерация: только вперед")
    print("     - Память: 1 указатель на узел (next)")
    
    print("\nВывод: Двусвязный список эффективнее для удаления,")
    print("       но требует больше памяти для хранения указателей.")