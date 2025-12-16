"""
Задание 5: Стек
Реализация стека на массиве и связном списке.
Использование стека для проверки корректности скобочной последовательности.
"""

# Класс для узла связного списка
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Стек на массиве (списке Python)
class ArrayStack:
    def __init__(self):
        self.data = []
    
    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
    
    def show(self):
        return self.data.copy()


# Стек на связном списке
class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.value
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size
    
    def show(self):
        result = []
        current = self.top
        while current:
            result.append(current.value)
            current = current.next
        return result


# Проверка скобочных последовательностей
def check_brackets(expression):
    stack = ArrayStack()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()


# Основная функция
if __name__ == "__main__":
    print("ДЕМОНСТРАЦИЯ РАБОТЫ СТЕКА")
    print("=" * 40)
    
    print("\n1. Стек на массиве:")
    print("-" * 20)
    
    arr_stack = ArrayStack()
    
    print("Добавляем числа в стек:")
    for i in [10, 20, 30, 40]:
        arr_stack.push(i)
        print(f"Добавили {i}. Стек: {arr_stack.show()}")
    
    print(f"\nВершина стека: {arr_stack.peek()}")
    print(f"Размер стека: {arr_stack.size()}")
    
    print("\nУдаляем элементы сверху:")
    for _ in range(2):
        item = arr_stack.pop()
        print(f"Удалили {item}. Стек: {arr_stack.show()}")
    
    print(f"\nПустой ли стек? {arr_stack.is_empty()}")
    
    print("\n\n2. Стек на связном списке:")
    print("-" * 25)
    
    list_stack = LinkedListStack()
    
    print("Добавляем слова в стек:")
    for word in ["первый", "второй", "третий"]:
        list_stack.push(word)
        print(f"Добавили '{word}'. Стек: {list_stack.show()}")
    
    print(f"\nВершина стека: '{list_stack.peek()}'")
    print(f"Размер стека: {list_stack.size()}")
    
    print("\nУдаляем элементы сверху:")
    for _ in range(2):
        item = list_stack.pop()
        print(f"Удалили '{item}'. Стек: {list_stack.show()}")
    
    print(f"\nПустой ли стек? {list_stack.is_empty()}")
    
    print("\n\n3. Проверка скобок:")
    print("-" * 20)
    
    examples = [
        ("(2+3)", True),
        ("([{}])", True),
        ("{[]()}", True),
        ("((())", False),
        ("([)]", False),
        ("])", False),
    ]
    
    for expr, should_be_correct in examples:
        result = check_brackets(expr)
        status = "✓ OK" if result == should_be_correct else "✗ Ошибка"
        correctness = "корректно" if result else "некорректно"
        print(f"{expr:15} -> {correctness:15} {status}")
    
    print("\n\n4. Как работает проверка скобок:")
    print("-" * 30)
    
    test = "( [ ] )"
    print(f"Пример: {test}")
    
    stack = ArrayStack()
    step = 1
    
    print("Пошагово:")
    for char in test.replace(" ", ""):
        if char in '([{':
            stack.push(char)
            print(f"  {char} - открывающая -> в стек")
            print(f"    Стек: {stack.show()}")
        elif char in ')]}':
            pairs = {')': '(', ']': '[', '}': '{'}
            expected = pairs[char]
            got = stack.pop()
            print(f"  {char} - закрывающая -> сравниваем с {expected}")
            print(f"    В стеке было: {got}")
            print(f"    Совпадает? {got == expected}")
    
    print(f"\nВ конце стек пустой? {stack.is_empty()}")
    print(f"Результат: {'Все скобки закрыты' if stack.is_empty() else 'Ошибка в скобках'}")
    
    print("\n" + "=" * 40)
    print("Демонстрация завершена!")