"""
Задание 12: Trie (углубление)
- хранение слов целиком
- подсчёт количества вариантов по префиксу  
- удаление слова
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""  # храним слово целиком
        self.word_count = 0  # количество слов в поддереве

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Вставка слова целиком."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_count += 1  # увеличиваем счетчик в каждом узле
        
        node.is_end = True
        node.word = word  # сохраняем слово целиком
    
    def search(self, word):
        """Поиск точного слова."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def prefix_count(self, prefix):
        """Подсчёт количества слов с заданным префиксом."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count  # используем сохраненный счетчик
    
    def delete(self, word):
        """Удаление слова из Trie."""
        if not self.search(word):
            return False
        
        # Сохраняем путь к слову
        path = []
        node = self.root
        
        for char in word:
            path.append((node, char))
            node = node.children[char]
        
        # Удаляем слово
        node.is_end = False
        node.word = ""
        
        # Уменьшаем счетчики и удаляем пустые узлы
        for node, char in reversed(path):
            node.word_count -= 1
            child = node.children[char]
            
            # Удаляем узел если он пустой и не является концом другого слова
            if not child.is_end and len(child.children) == 0:
                del node.children[char]
        
        return True


def main():
    print("=" * 60)
    print("TRIE (УГЛУБЛЕНИЕ)")
    print("=" * 60)
    
    trie = Trie()
    
    # 1. Вставка слов
    print("\n1. ВСТАВКА СЛОВ:")
    words = ["cat", "car", "card", "dog", "door", "do", "apple"]
    for word in words:
        trie.insert(word)
        print(f"   Добавлено: '{word}'")
    
    # 2. Проверка хранения слов целиком
    print("\n2. ПРОВЕРКА ХРАНЕНИЯ СЛОВ ЦЕЛИКОМ:")
    test_word = "apple"
    # Ищем узел для слова "apple"
    node = trie.root
    for char in test_word:
        if char in node.children:
            node = node.children[char]
    print(f"   В узле для '{test_word}' хранится: '{node.word}'")
    print(f"   Это конец слова: {node.is_end}")
    
    # 3. Подсчёт слов по префиксу
    print("\n3. ПОДСЧЁТ СЛОВ ПО ПРЕФИКСУ:")
    prefixes = ["ca", "car", "do", "app", "x"]
    for prefix in prefixes:
        count = trie.prefix_count(prefix)
        print(f"   Префикс '{prefix}': {count} слов")
    
    # 4. Удаление слова
    print("\n4. УДАЛЕНИЕ СЛОВА:")
    print("   Удаляем 'car':")
    if trie.delete("car"):
        print("   Удаление успешно")
    
    print("\n   Результаты после удаления:")
    print(f"   'car' найден: {trie.search('car')}")
    print(f"   'card' найден: {trie.search('card')}")
    print(f"   Префикс 'ca' теперь: {trie.prefix_count('ca')} слов")
    print(f"   Префикс 'car' теперь: {trie.prefix_count('car')} слов")
    
    # 5. Попытка удалить несуществующее слово
    print("\n5. ПОПЫТКА УДАЛИТЬ НЕСУЩЕСТВУЮЩЕЕ СЛОВО:")
    print(f"   Удаляем 'unknown': {trie.delete('unknown')}")


if __name__ == "__main__":
    main()