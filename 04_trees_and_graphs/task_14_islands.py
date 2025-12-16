"""
Задание 14: Задача "Острова"
Дан двумерный массив 0/1. Найти количество "островов" (компонент связности).
Использовать DFS или BFS.
"""

from collections import deque

class IslandCounter:
    """Класс для подсчета островов в бинарной матрице."""
    
    def __init__(self, grid):
        """
        Инициализация с заданной сеткой.
        
        Args:
            grid: Двумерный список из 0 и 1
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
    
    def count_islands_bfs(self):
        """Подсчет островов с использованием BFS.
        
        Returns:
            Количество островов
        """
        if self.rows == 0 or self.cols == 0:
            return 0
        
        visited = [[False] * self.cols for _ in range(self.rows)]
        islands = 0
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1 and not visited[i][j]:
                    islands += 1
                    self._bfs(i, j, visited)
        
        return islands
    
    def _bfs(self, start_i, start_j, visited):
        """BFS для посещения всего острова."""
        queue = deque([(start_i, start_j)])
        visited[start_i][start_j] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            i, j = queue.popleft()
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                
                if (0 <= ni < self.rows and 0 <= nj < self.cols and
                    self.grid[ni][nj] == 1 and not visited[ni][nj]):
                    
                    visited[ni][nj] = True
                    queue.append((ni, nj))
    
    def count_islands_dfs(self):
        """Подсчет островов с использованием DFS.
        
        Returns:
            Количество островов
        """
        if self.rows == 0 or self.cols == 0:
            return 0
        
        visited = [[False] * self.cols for _ in range(self.rows)]
        islands = 0
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1 and not visited[i][j]:
                    islands += 1
                    self._dfs(i, j, visited)
        
        return islands
    
    def _dfs(self, i, j, visited):
        """DFS для посещения всего острова."""
        if (i < 0 or i >= self.rows or j < 0 or j >= self.cols or
            self.grid[i][j] == 0 or visited[i][j]):
            return
        
        visited[i][j] = True
        
        # Рекурсивно посещаем соседей
        self._dfs(i - 1, j, visited)  # вверх
        self._dfs(i + 1, j, visited)  # вниз
        self._dfs(i, j - 1, visited)  # влево
        self._dfs(i, j + 1, visited)  # вправо
    
    def print_grid(self):
        """Выводит сетку в читаемом формате."""
        print("Сетка:")
        for row in self.grid:
            print(" ".join("■" if cell == 1 else "·" for cell in row))
        print()


def demonstrate():
    """Демонстрация работы алгоритмов."""
    print("=" * 50)
    print("ЗАДАЧА 'ОСТРОВА'")
    print("=" * 50)
    
    # Пример 1: Простая сетка
    print("\nПример 1:")
    grid1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    
    counter1 = IslandCounter(grid1)
    counter1.print_grid()
    
    print(f"Количество островов (BFS): {counter1.count_islands_bfs()}")
    print(f"Количество островов (DFS): {counter1.count_islands_dfs()}")
    
    # Пример 2: Сетка без островов
    print("\nПример 2 (только вода):")
    grid2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    
    counter2 = IslandCounter(grid2)
    counter2.print_grid()
    print(f"Количество островов: {counter2.count_islands_bfs()}")
    
    # Пример 3: Один большой остров
    print("\nПример 3 (один остров):")
    grid3 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    
    counter3 = IslandCounter(grid3)
    counter3.print_grid()
    print(f"Количество островов: {counter3.count_islands_bfs()}")
    
    # Пример 4: Каждая клетка - отдельный остров
    print("\nПример 4 (много островов):")
    grid4 = [
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    
    counter4 = IslandCounter(grid4)
    counter4.print_grid()
    print(f"Количество островов: {counter4.count_islands_dfs()}")
    
    print("\n" + "=" * 50)
    print("СРАВНЕНИЕ АЛГОРИТМОВ:")
    print("  BFS:")
    print("    + Использует очередь (deque)")
    print("    + Не вызывает переполнение стека")
    print("    + Находит кратчайшие пути")
    print("    - Требует больше памяти")
    
    print("\n  DFS:")
    print("    + Простая рекурсивная реализация")
    print("    + Экономит память (глубина стека)")
    print("    - Может вызвать переполнение стека")
    print("    - Не гарантирует кратчайший путь")
    
    print("\n  Оба алгоритма:")
    print("    - Сложность: O(rows × cols)")
    print("    - Память: O(rows × cols) для visited")
    print("    - Используют поиск в 4 направлениях")


# Запуск демонстрации
if __name__ == "__main__":
    demonstrate()