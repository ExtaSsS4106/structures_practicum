"""
Задание 10: Trie + HashMap: автодополнение
Реализация Trie для хранения слов.
Реализация поиска по префиксу: метод autocomplete(prefix).
Использование HashMap + Trie для хранения слов и их частот.
Предложение подсказок в порядке убывания частоты.
"""

class TrieNode:
    """Узел префиксного дерева (Trie)."""
    def __init__(self):
        self.children = {}      # Дочерние узлы: символ -> TrieNode
        self.is_end = False    # Конец слова
        self.freq = 0          # Частота слова


class Trie:
    """Префиксное дерево (Trie) для автодополнения."""
    
    def __init__(self):
        self.root = TrieNode()
        self.word_freq = {}    # HashMap для хранения частот слов
    
    def insert(self, word: str, freq: int = 1) -> None:
        """Добавляет слово в Trie и обновляет HashMap."""
        node = self.root
        word_lower = word.lower()
        
        for char in word_lower:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end = True
        node.freq += freq
        
        # Обновляем HashMap
        self.word_freq[word_lower] = node.freq
    
    def _collect_words(self, node, prefix: str, results: list) -> None:
        """Собирает все слова из поддерева."""
        if node.is_end:
            results.append((prefix, node.freq))
        
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, results)
    
    def autocomplete(self, prefix: str, limit: int = 10) -> list:
        """Находит слова по префиксу и сортирует по частоте."""
        node = self.root
        
        # Идем по префиксу
        for char in prefix.lower():
            if char not in node.children:
                return []  # Префикс не найден
            node = node.children[char]
        
        # Собираем все слова с этим префиксом
        results = []
        self._collect_words(node, prefix.lower(), results)
        
        # Сортируем по частоте (убывание)
        results.sort(key=lambda x: x[1], reverse=True)
        
        # Возвращаем слова (без частот)
        return [word for word, _ in results[:limit]]


def main():
    """Демонстрация работы системы автодополнения."""
    print("=" * 60)
    print("СИСТЕМА АВТОДОПОЛНЕНИЯ (Trie + HashMap)")
    print("=" * 60)
    
    # Создаем Trie
    trie = Trie()
    
    # Добавляем слова с частотами (имитация популярных запросов)
    print("\nЗагрузка слов в систему...")
    
    # Слова с частотами (чем больше частота, тем популярнее слово)
    words_with_freq = [
        ("python", 150),
        ("programming", 120),
        ("programmer", 80),
        ("program", 100),
        ("project", 90),
        ("problem", 70),
        ("product", 85),
        ("progress", 60),
        ("java", 130),
        ("javascript", 110),
        ("web", 140),
        ("website", 75),
        ("window", 50),
        ("windows", 45),
        ("data", 95),
        ("database", 65),
        ("development", 88),
        ("design", 72),
    ]
    
    for word, freq in words_with_freq:
        trie.insert(word, freq)
        print(f"  Добавлено: {word} (частота: {freq})")
    
    print(f"\nВсего уникальных слов: {len(trie.word_freq)}")
    
    # Демонстрация работы autocomplete
    print("\n" + "="*60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ АВТОДОПОЛНЕНИЯ")
    print("="*60)
    
    test_cases = [
        ("pro", "Поиск слов с префиксом 'pro'"),
        ("p", "Поиск слов с префиксом 'p'"),
        ("web", "Поиск слов с префиксом 'web'"),
        ("jav", "Поиск слов с префиксом 'jav'"),
        ("dat", "Поиск слов с префиксом 'dat'"),
        ("xyz", "Поиск несуществующего префикса 'xyz'"),
    ]
    
    for prefix, description in test_cases:
        print(f"\n{description}:")
        print("-" * 40)
        
        suggestions = trie.autocomplete(prefix, 5)
        
        if suggestions:
            print(f"Найдено {len(suggestions)} слов:")
            for i, word in enumerate(suggestions, 1):
                freq = trie.word_freq.get(word, 0)
                print(f"  {i}. {word:<15} [частота: {freq}]")
        else:
            print(f"Слова с префиксом '{prefix}' не найдены")
    
    # Пример интерактивного использования
    print("\n" + "="*60)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ (пример)")
    print("="*60)
    
    # Симулируем ввод пользователя
    user_inputs = ["pyt", "de", "w", "prog"]
    
    for user_prefix in user_inputs:
        print(f"\nПользователь ввел: '{user_prefix}'")
        suggestions = trie.autocomplete(user_prefix, 3)
        
        if suggestions:
            print("Система предлагает:")
            for word in suggestions:
                freq = trie.word_freq.get(word, 0)
                print(f"  • {word} ({freq} запросов)")
        else:
            print("  Нет предложений")


if __name__ == "__main__":
    main()