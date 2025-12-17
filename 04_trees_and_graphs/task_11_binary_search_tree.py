"""
Задание 11: Бинарное дерево поиска (BST)
Реализовать:
- вставку
- поиск  
- удаление
- обходы: in-order, pre-order, post-order
- проверку баланса
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Вставка значения в дерево."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)
    
    def search(self, value):
        """Поиск значения в дереве."""
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)
    
    def inorder(self):
        """In-order обход (левый-корень-правый)."""
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)
    
    def preorder(self):
        """Pre-order обход (корень-левый-правый)."""
        result = []
        self._preorder_traversal(self.root, result)
        return result
    
    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
    
    def postorder(self):
        """Post-order обход (левый-правый-корень)."""
        result = []
        self._postorder_traversal(self.root, result)
        return result
    
    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)
    
    def is_balanced(self):
        """Проверка, является ли дерево сбалансированным."""
        return self._check_balance(self.root) != -1
    
    def _check_balance(self, node):
        if node is None:
            return 0
        
        left_height = self._check_balance(node.left)
        if left_height == -1:
            return -1
        
        right_height = self._check_balance(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    def delete(self, value):
        """Удаление значения из дерева."""
        self.root = self._delete(self.root, value)
    
    def _delete(self, node, value):
        """Вспомогательный рекурсивный метод для удаления."""
        if node is None:
            return node
        
        # Поиск узла для удаления
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Узел найден. Теперь три случая:
            
            # Случай 1: Узел без потомков или с одним потомком
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Случай 2: Узел с двумя потомками
            # Находим преемника (минимальный элемент в правом поддереве)
            successor = self._find_min(node.right)
            node.value = successor.value  # Копируем значение преемника
            node.right = self._delete(node.right, successor.value)  # Удаляем преемника
        
        return node
    
    def _find_min(self, node):
        """Находит минимальный элемент в поддереве."""
        current = node
        while current.left is not None:
            current = current.left
        return current


def main():
    print("=" * 60)
    print("БИНАРНОЕ ДЕРЕВО ПОИСКА (BST) - НЕСБАЛАНСИРОВАННОЕ")
    print("=" * 60)
    
    # 1. Создание НЕСБАЛАНСИРОВАННОГО дерева
    bst = BinarySearchTree()
    
    print("\n1. СОЗДАНИЕ НЕСБАЛАНСИРОВАННОГО ДЕРЕВА:")
    print("   Вставляем значения по порядку [1, 2, 3, 4, 5, 6, 7]:")
    values = [1, 2, 3, 4, 5, 6, 7]  # Вставляем по порядку - создаем вырожденное дерево
    for val in values:
        bst.insert(val)
    
    # 2. Обходы
    print("\n2. ОБХОДЫ дерева:")
    print(f"   In-order (отсортировано):  {bst.inorder()}")
    print(f"   Pre-order:                 {bst.preorder()}")
    print(f"   Post-order:                {bst.postorder()}")
    
    # 3. Проверка баланса
    print(f"\n3. ПРОВЕРКА БАЛАНСА:")
    balanced = bst.is_balanced()
    print(f"   Дерево сбалансировано: {'ДА' if balanced else 'НЕТ'}")
    print(f"   Дерево ВЫРОДИЛОСЬ в связный список!")
    
    # 4. Поиск
    print(f"\n4. ПОИСК:")
    print(f"   4: {'найден' if bst.search(4) else 'не найден'}")
    print(f"   8: {'найден' if bst.search(8) else 'не найден'}")
    
    # 5. ДЕМОНСТРАЦИЯ УДАЛЕНИЯ (ДОБАВЛЕННЫЙ КОД)
    print(f"\n5. ДЕМОНСТРАЦИЯ УДАЛЕНИЯ:")
    
    # Удаление листа (значение 7)
    print(f"\n   а) Удаление листа (значение 7):")
    print(f"      До удаления: {bst.inorder()}")
    bst.delete(7)  # Вызов метода удаления
    print(f"      После удаления: {bst.inorder()}")
    
    # Удаление узла с одним потомком (значение 6)
    print(f"\n   б) Удаление узла с одним потомком (значение 6):")
    print(f"      До удаления: {bst.inorder()}")
    bst.delete(6)  # Вызов метода удаления
    print(f"      После удаления: {bst.inorder()}")
    
    # Проверка поиска после удалений
    print(f"\n   в) Проверка поиска после удалений:")
    print(f"      7: {'найден' if bst.search(7) else 'не найден'} (был удален)")
    print(f"      6: {'найден' if bst.search(6) else 'не найден'} (был удален)")
    print(f"      5: {'найден' if bst.search(5) else 'не найден'}")
    
    # 6. Создание сбалансированного дерева для сравнения
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ: СБАЛАНСИРОВАННОЕ vs НЕСБАЛАНСИРОВАННОЕ")
    print("=" * 60)
    
    # Сбалансированное дерево
    balanced_bst = BinarySearchTree()
    print("\nСБАЛАНСИРОВАННОЕ ДЕРЕВО:")
    bal_values = [4, 2, 6, 1, 3, 5, 7]  # Вставляем в порядке создания сбалансированного дерева
    for val in bal_values:
        balanced_bst.insert(val)
    
    print(f"   Значения: {bal_values}")
    print(f"   In-order: {balanced_bst.inorder()}")
    print(f"   Сбалансировано: {'ДА' if balanced_bst.is_balanced() else 'НЕТ'}")
    
    # Несбалансированное дерево
    print("\nНЕСБАЛАНСИРОВАННОЕ ДЕРЕВО:")
    print(f"   Исходные значения: {values}")
    print(f"   Текущее состояние: {bst.inorder()}")
    print(f"   Сбалансировано: {'ДА' if bst.is_balanced() else 'НЕТ'}")
    
    # Демонстрация удаления в сбалансированном дереве
    print(f"\n   Удаление в сбалансированном дереве (значение 2):")
    print(f"      До удаления: {balanced_bst.inorder()}")
    balanced_bst.delete(2)
    print(f"      После удаления: {balanced_bst.inorder()}")
    print(f"      Сбалансировано: {'ДА' if balanced_bst.is_balanced() else 'НЕТ'}")


if __name__ == "__main__":
    main()
