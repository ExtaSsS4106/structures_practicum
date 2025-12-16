"""
Задание 3: Односвязный список
Реализовать:
- вставку в начало/конец,
- удаление по значению,
- поиск по значению,
- разворот списка in-place.
Сравнить операции вставки/удаления с массивом.
"""

class Node:
    """Узел односвязного списка."""
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    """Односвязный список с базовыми операциями."""
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def pushFront(self, value) -> None:
        """Вставка в начало. Сложность: O(1)"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def pushBack(self, value) -> None:
        """Вставка в конец. Сложность: O(n) без tail, O(1) с tail"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def removeByValue(self, value) -> bool:
        """Удаление по значению. Сложность: O(n)"""
        if not self.head:
            return False
        
        # Удаление головы
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return True
        
        # Поиск и удаление в середине/конце
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, value) -> bool:
        """Поиск по значению. Сложность: O(n)"""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def reverse(self) -> None:
        """Разворот списка in-place. Сложность: O(n)"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def __str__(self) -> str:
        """Представление списка для вывода."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements) if elements else "Пусто"


# Демонстрация работы
if __name__ == "__main__":
    print("=== Демонстрация односвязного списка ===\n")
    
    # Создание и заполнение списка
    sll = SinglyLinkedList()
    
    print("1. Вставка в начало и конец:")
    sll.pushFront(3)
    sll.pushFront(2)
    sll.pushFront(1)
    sll.pushBack(4)
    sll.pushBack(5)
    print(f"   Список: {sll}")
    
    print("\n2. Удаление по значению:")
    print(f"   Удаляем 3: {'успешно' if sll.removeByValue(3) else 'не найдено'}")
    print(f"   Удаляем 10: {'успешно' if sll.removeByValue(10) else 'не найдено'}")
    print(f"   Список после удаления: {sll}")
    
    print("\n3. Поиск по значению:")
    print(f"   Ищем 2: {'найдено' if sll.find(2) else 'не найдено'}")
    print(f"   Ищем 10: {'найдено' if sll.find(10) else 'не найдено'}")
    
    print("\n4. Разворот списка:")
    print(f"   До разворота: {sll}")
    sll.reverse()
    print(f"   После разворота: {sll}")
    
    print("\n=== Сравнение со списком Python (массивом) ===\n")
    
    import time
    
    # Тест вставки в начало
    print("Вставка 10000 элементов в начало:")
    
    # Односвязный список
    start = time.time()
    test_list = SinglyLinkedList()
    for i in range(10000):
        test_list.pushFront(i)
    list_time = time.time() - start
    print(f"  Односвязный список: {list_time:.4f} сек (O(1) на операцию)")
    
    # Список Python (массив)
    start = time.time()
    test_array = []
    for i in range(10000):
        test_array.insert(0, i)  # insert(0) = O(n)
    array_time = time.time() - start
    print(f"  Массив (Python list): {array_time:.4f} сек (O(n) на операцию)")
    print(f"  Ускорение: {array_time/list_time:.1f}x в пользу списка")
    
    print("\nВывод: Односвязный список эффективнее для частых вставок в начало,")
    print("       но уступает массиву в произвольном доступе (O(n) vs O(1)).")