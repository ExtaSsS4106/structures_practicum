"""
Задание 13: Графы
Хранение графов: матрица смежности и список смежности.
Реализация алгоритмов: BFS, DFS, поиск кратчайшего пути в невзвешенном графе.
"""

from collections import deque, defaultdict

class Graph:
    """Класс для представления графа."""
    
    def __init__(self, directed=False):
        """Инициализация графа."""
        self.directed = directed
        self.vertices = set()
        self.adj_list = defaultdict(list)
        self.adj_matrix = None
    
    def add_edge(self, u, v):
        """Добавление ребра между вершинами."""
        self.vertices.add(u)
        self.vertices.add(v)
        
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)
    
    def build_adjacency_matrix(self):
        """Построение матрицы смежности."""
        if not self.vertices:
            return
        
        sorted_vertices = sorted(self.vertices)
        n = len(sorted_vertices)
        self.adj_matrix = [[0] * n for _ in range(n)]
        vertex_to_index = {vertex: i for i, vertex in enumerate(sorted_vertices)}
        
        for u in sorted_vertices:
            for v in self.adj_list[u]:
                i = vertex_to_index[u]
                j = vertex_to_index[v]
                self.adj_matrix[i][j] = 1
                if not self.directed:
                    self.adj_matrix[j][i] = 1
    
    def bfs(self, start):
        """Обход графа в ширину (BFS)."""
        if start not in self.vertices:
            return []
        
        visited = set([start])
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Обход графа в глубину (DFS) - итеративная версия."""
        if start not in self.vertices:
            return []
        
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                for neighbor in reversed(self.adj_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def shortest_path_unweighted(self, start, end):
        """Поиск кратчайшего пути в невзвешенном графе (BFS)."""
        if start not in self.vertices or end not in self.vertices:
            return []
        
        if start == end:
            return [start]
        
        visited = set([start])
        queue = deque([start])
        parent = {start: None}
        
        while queue:
            vertex = queue.popleft()
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = vertex
                    
                    if neighbor == end:
                        # Восстанавливаем путь
                        path = []
                        current = end
                        while current is not None:
                            path.append(current)
                            current = parent[current]
                        return path[::-1]
                    
                    queue.append(neighbor)
        
        return []  # Путь не найден
    
    def print_adjacency_list(self):
        """Вывод списка смежности."""
        print("Список смежности:")
        for vertex in sorted(self.vertices):
            neighbors = sorted(self.adj_list[vertex])
            print(f"  {vertex}: {neighbors}")
    
    def print_adjacency_matrix(self):
        """Вывод матрицы смежности."""
        if self.adj_matrix is None:
            self.build_adjacency_matrix()
        
        if not self.adj_matrix:
            return
        
        print("Матрица смежности:")
        sorted_vertices = sorted(self.vertices)
        
        # Заголовок
        print("   " + " ".join(f"{v:2}" for v in sorted_vertices))
        
        # Строки матрицы
        for i, vertex in enumerate(sorted_vertices):
            row = " ".join(f"{self.adj_matrix[i][j]:2}" for j in range(len(sorted_vertices)))
            print(f"{vertex:2}: {row}")


def demonstrate():
    """Демонстрация работы с графами."""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ АЛГОРИТМОВ НА ГРАФАХ")
    print("=" * 50)
    
    # 1. Создание графа
    print("\n1. СОЗДАНИЕ ГРАФА")
    g = Graph(directed=False)
    
    # Добавляем ребра (граф из примера)
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (5, 7), (6, 7)]
    for u, v in edges:
        g.add_edge(u, v)
    
    # 2. Вывод представлений графа
    print("\n2. ПРЕДСТАВЛЕНИЯ ГРАФА")
    g.print_adjacency_list()
    print()
    g.print_adjacency_matrix()
    
    # 3. Обходы графа
    print("\n3. ОБХОДЫ ГРАФА")
    
    start_vertex = 1
    print(f"BFS начиная с вершины {start_vertex}: {g.bfs(start_vertex)}")
    print(f"DFS начиная с вершины {start_vertex}: {g.dfs(start_vertex)}")
    
    # 4. Поиск кратчайшего пути
    print("\n4. ПОИСК КРАТЧАЙШЕГО ПУТИ")
    start, end = 1, 7
    path = g.shortest_path_unweighted(start, end)
    if path:
        print(f"Кратчайший путь от {start} до {end}: {' → '.join(map(str, path))}")
        print(f"Длина пути: {len(path)-1} ребер")
    else:
        print(f"Путь от {start} до {end} не найден")
    
    # 5. Сравнение представлений
    print("\n5. СРАВНЕНИЕ ПРЕДСТАВЛЕНИЙ")
    print("Матрица смежности:")
    print("  + Быстрая проверка наличия ребра (O(1))")
    print("  - Требует O(V²) памяти")
    print("  - Медленный поиск соседей (O(V))")
    print("\nСписок смежности:")
    print("  + Экономит память для разреженных графов (O(V+E))")
    print("  + Быстрый перебор соседей (O(deg(v)))")
    print("  - Медленная проверка наличия ребра (O(deg(v)))")


# Запуск демонстрации
if __name__ == "__main__":
    demonstrate()