"""
Задание 9: Частотный словарь
Построение HashMap частот встречаемости слов в тексте.
Вывод топ-10 самых частых слов.
Сравнение времени построения при плохой и хорошей хэш-функции.
"""

import time
import re
import random

class CustomHashMap:
    """Кастомная HashMap для демонстрации разницы хэш-функций."""
    
    def __init__(self, hash_func_type: str = "good"):
        self.capacity = 1000
        self.hash_func_type = hash_func_type
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        
    def _hash_good(self, key: str) -> int:
        """Хорошая хэш-функция."""
        h = 0
        for char in key:
            h = (h * 31 + ord(char)) % self.capacity
        return h
    
    def _hash_bad(self, key: str) -> int:
        """Плохая хэш-функция (всегда 0)."""
        return 0
    
    def _get_hash(self, key: str) -> int:
        if self.hash_func_type == "bad":
            return self._hash_bad(key)
        return self._hash_good(key)
    
    def increment(self, key: str) -> None:
        """Увеличивает счетчик слова на 1."""
        index = self._get_hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, v + 1)
                return
        
        bucket.append((key, 1))
        self.size += 1
    
    def get_collisions(self) -> int:
        """Считает коллизии."""
        collisions = 0
        for bucket in self.buckets:
            if len(bucket) > 1:
                collisions += len(bucket) - 1
        return collisions


def generate_test_text(word_count: int = 20000) -> str:
    """Генерирует тестовый текст."""
    common_words = ['дом', 'кот', 'собака', 'человек', 'город', 'улица', 'машина',
                    'дерево', 'солнце', 'луна', 'вода', 'земля', 'огонь', 'воздух',
                    'книга', 'школа', 'работа', 'день', 'ночь', 'утро', 'вечер']
    
    text_words = []
    for _ in range(word_count):
        if random.random() < 0.7:
            text_words.append(random.choice(common_words))
        else:
            length = random.randint(3, 8)
            word = ''.join(chr(random.randint(97, 122)) for _ in range(length))
            text_words.append(word)
    
    return " ".join(text_words)


def process_text_with_hashmap(text: str, hash_type: str):
    """Обрабатывает текст с указанным типом хэш-функции."""
    print(f"\n{'='*60}")
    print(f"Тест с {hash_type.upper()} хэш-функцией")
    print('='*60)
    
    # Создаем HashMap
    hashmap = CustomHashMap(hash_func_type=hash_type)
    
    # Разбиваем на слова
    words = re.findall(r'\b[a-zA-Zа-яА-Я]+\b', text.lower())
    
    # Измеряем время
    start_time = time.time()
    
    for word in words:
        hashmap.increment(word)
    
    processing_time = time.time() - start_time
    
    # Собираем топ слов
    all_items = []
    for bucket in hashmap.buckets:
        all_items.extend(bucket)
    
    top_words = sorted(all_items, key=lambda x: x[1], reverse=True)[:10]
    
    # Выводим результаты
    print(f"Время обработки: {processing_time:.4f} сек")
    print(f"Всего слов: {len(words):,}")
    print(f"Уникальных слов: {hashmap.size:,}")
    print(f"Коллизии: {hashmap.get_collisions():,}")
    
    if hash_type == "bad":
        print(f"ВСЕ слова в одной корзине! Поиск O(n) вместо O(1)")
    
    return processing_time, top_words


def main():
    """Основная функция."""
    print("ЗАДАНИЕ 9: СРАВНЕНИЕ ХЭШ-ФУНКЦИЙ")
    print("="*60)
    
    # Генерируем текст
    print("\nГенерация тестового текста (20,000 слов)...")
    text = generate_test_text(20000)
    words = re.findall(r'\b[a-zA-Zа-яА-Я]+\b', text.lower())
    print(f"Текст готов: {len(words):,} слов")
    
    # Тест с плохой хэш-функцией
    time_bad, top_bad = process_text_with_hashmap(text, "bad")
    
    # Тест с хорошей хэш-функцией
    time_good, top_good = process_text_with_hashmap(text, "good")
    
    # Сравнение результатов
    print("\n" + "="*60)
    print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ")
    print("="*60)
    
    print(f"\n{'Параметр':<25} {'Плохая':<15} {'Хорошая':<15} {'Отношение':<10}")
    print("-"*65)
    print(f"{'Время (сек)':<25} {time_bad:<15.4f} {time_good:<15.4f} {time_bad/time_good:<10.1f}x")
    print(f"{'Скорость (слов/сек)':<25} {len(words)/time_bad:<15,.0f} {len(words)/time_good:<15,.0f} {time_good/time_bad:<10.1f}x")
    
    # Вывод топ-10 слов
    print("\n" + "="*60)
    print("ТОП-10 САМЫХ ЧАСТЫХ СЛОВ")
    print("="*60)
    
    print(f"\n{'№':<4} {'Слово':<15} {'Частота':<10}")
    print("-"*30)
    
    for i, (word, freq) in enumerate(top_good, 1):
        print(f"{i:<4} {word:<15} {freq:<10}")
    

    
    # Заключение
    print("\n" + "="*60)
    print("ВЫВОД")
    print("="*60)
    
    print(f"""
    Результат: Плохая хэш-функция медленнее в {time_bad/time_good:.1f} раз!
    
    Выводы:
    1. Хэш-функция должна равномерно распределять ключи
    2. Коллизии замедляют работу в разы
    3. Плохая хэш-функция превращает HashMap в список
    4. Всегда тестируйте хэш-функции на реальных данных
    
    ТЗ выполнено:
    ✓ Построен частотный словарь
    ✓ Реализованы плохая и хорошая хэш-функции
    ✓ Выведен топ-10 самых частых слов
    ✓ Сравнено время построения
    """)


if __name__ == "__main__":
    main()