"""
Задание 8: Хэш-таблица с методом цепочек для разрешения коллизий
"""

class HashTableEntry:
    """Элемент хэш-таблицы (узел цепочки)."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.key}:{self.value}"


class HashMap:
    """Хэш-таблица с методом разрешения коллизий через цепочки."""
    
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.collisions_count = 0
    
    def _hash(self, key):
        """Хэш-функция для строк."""
        key_str = str(key)
        hash_value = 0
        prime = 31
        
        for char in key_str:
            hash_value = (hash_value * prime + ord(char)) % self.capacity
        
        return hash_value
    
    def _resolve_collision(self, bucket, key, value, operation='put'):
        """
        Метод разрешения коллизий (цепочки).
        """
        current = bucket
        prev = None
        
        if operation == 'put':
            while current:
                if current.key == key:
                    current.value = value
                    return bucket, False
                prev = current
                current = current.next
            
            new_entry = HashTableEntry(key, value)
            if prev:
                prev.next = new_entry
            else:
                new_entry.next = bucket
                bucket = new_entry
            return bucket, True
            
        elif operation == 'get':
            while current:
                if current.key == key:
                    return current.value
                current = current.next
            return None
            
        elif operation == 'remove':
            while current:
                if current.key == key:
                    if prev:
                        prev.next = current.next
                    else:
                        bucket = current.next
                    return bucket, True
                prev = current
                current = current.next
            return bucket, False
    
    def _get_bucket_chain(self, index):
        """Возвращает строковое представление цепочки в ячейке."""
        current = self.buckets[index]
        if not current:
            return "пусто"
        
        elements = []
        while current:
            elements.append(str(current))
            current = current.next
        
        return " -> ".join(elements)
    
    def put(self, key, value):
        """Добавление или обновление элемента."""
        index = self._hash(key)
        
        if self.buckets[index] is not None:
            self.collisions_count += 1
        
        self.buckets[index], added = self._resolve_collision(
            self.buckets[index], key, value, 'put'
        )
        
        if added:
            self.size += 1
    
    def get(self, key):
        """Получение значения по ключу."""
        index = self._hash(key)
        return self._resolve_collision(self.buckets[index], key, None, 'get')
    
    def remove(self, key):
        """Удаление элемента по ключу."""
        index = self._hash(key)
        self.buckets[index], removed = self._resolve_collision(
            self.buckets[index], key, None, 'remove'
        )
        
        if removed:
            self.size -= 1
        return removed
    
    def visualize(self):
        """Визуализация всей таблицы."""
        print("\nСостояние хэш-таблицы:")
        print(f"Емкость: {self.capacity}")
        print(f"Элементов: {self.size}")
        print(f"Коллизии: {self.collisions_count}")
        print(f"Коэффициент загрузки: {self.size/self.capacity:.1%}")
        
        print("\nСодержимое таблицы:")
        for i in range(self.capacity):
            print(f"[{i}]: {self._get_bucket_chain(i)}")


# Демонстрация работы
def main():
    print("="*60)
    print("ДЕМОНСТРАЦИЯ ХЭШ-ТАБЛИЦЫ")
    print("="*60)
    
    # Создаем таблицу с маленькой емкостью для наглядности коллизий
    hash_table = HashMap(initial_capacity=7)
    
    print("\n1. Добавление элементов (показываем коллизии):")
    print("-" * 50)
    
    # Пример несвязанных данных: информация о студентах
    test_data = [
        ("id_101", "Иван Петров"),
        ("id_102", "Мария Сидорова"),
        ("id_103", "Алексей Иванов"),
        ("id_104", "Екатерина Смирнова"),
        ("id_105", "Дмитрий Кузнецов"),
        ("id_106", "Ольга Васильева"),
        ("id_107", "Сергей Попов"),
        ("id_108", "Анна Федорова"),
    ]
    
    for key, value in test_data:
        print(f"put('{key}', '{value}')")
        hash_table.put(key, value)
    
    # Визуализация после всех вставок
    hash_table.visualize()
    
    print("\n\n2. Поиск элементов:")
    print("-" * 50)
    
    # Поиск существующих и несуществующих записей
    search_keys = ["id_101", "id_105", "id_999", "id_103"]
    for key in search_keys:
        result = hash_table.get(key)
        if result is None:
            print(f"get('{key}') = не найден")
        else:
            print(f"get('{key}') = '{result}'")
    
    print("\n\n3. Обновление элемента:")
    print("-" * 50)
    
    # Обновляем запись
    print("put('id_102', 'Мария СИДОРОВА (изменено)')")
    hash_table.put("id_102", "Мария СИДОРОВА (изменено)")
    print(f"get('id_102') = '{hash_table.get('id_102')}'")
    
    print("\n\n4. Удаление элементов:")
    print("-" * 50)
    
    # Удаление существующих и несуществующих записей
    remove_keys = ["id_104", "id_107", "id_999"]
    for key in remove_keys:
        success = hash_table.remove(key)
        print(f"remove('{key}') = {'успешно' if success else 'не найден'}")
    
    # Финальная визуализация
    print("\n\n5. Финальное состояние таблицы:")
    print("-" * 50)
    hash_table.visualize()
    
    print("\n" + "="*60)
    print("ВЫВОД:")
    print("="*60)
    print("1. Хэш-функция преобразует строковые ключи в индексы массива")
    print("2. При коллизии (одинаковый индекс) элементы хранятся в цепочке")
    print("3. Метод цепочек позволяет хранить несколько элементов в одной ячейке")
    print("4. Операции put/get/remove ищут элемент в цепочке при необходимости")
    print("5. В среднем случае сложность операций O(1)")
    print("="*60)


if __name__ == "__main__":
    main()