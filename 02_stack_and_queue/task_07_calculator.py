"""
Задание 7. Задача "Калькулятор"
Считать выражение в инфиксной форме.
Используя стек, преобразовать в обратную польскую нотацию (ОПН).
Вычислить результат.
"""

class Stack:
    """Реализация стека для алгоритма преобразования."""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)


class Calculator:
    """Калькулятор с преобразованием в обратную польскую нотацию."""
    
    def __init__(self):
        # Приоритеты операторов (чем выше число, тем выше приоритет)
        self.priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,  # возведение в степень
            'u-': 4  # унарный минус
        }
    
    def tokenize(self, expression):
        """Разбивает выражение на токены (числа, операторы, скобки)."""
        tokens = []
        i = 0
        n = len(expression)
        
        print("Шаг 1: Разбиение на токены")
        print("=" * 50)
        
        while i < n:
            # Пропускаем пробелы
            if expression[i].isspace():
                i += 1
                continue
            
            # Обработка чисел (включая десятичные)
            if expression[i].isdigit() or expression[i] == '.':
                j = i
                while j < n and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                num_str = expression[i:j]
                tokens.append(float(num_str))
                print(f"  Найдено число: {num_str}")
                i = j
            
            # Обработка операторов и скобок
            else:
                tokens.append(expression[i])
                if expression[i] in '+-*/^()':
                    print(f"  Найден оператор/скобка: '{expression[i]}'")
                i += 1
        
        print(f"Итоговые токены: {tokens}")
        print("=" * 50)
        return tokens
    
    def infix_to_rpn(self, expression):
        """Преобразует инфиксную запись в обратную польскую нотацию."""
        
        print(f"\nВыражение: {expression}")
        print("\nШАГ 2: ПРЕОБРАЗОВАНИЕ В ОБРАТНУЮ ПОЛЬСКУЮ НОТАЦИЮ")
        print("=" * 50)
        
        tokens = self.tokenize(expression)
        output = []     # Выходная очередь для ОПН
        stack = Stack() # Стек для операторов
        prev_token = None
        
        print("\nПроцесс преобразования:")
        print("-" * 60)
        print(f"{'Токен':<10} {'Действие':<25} {'Стек':<15} {'Выход':<20}")
        print("-" * 60)
        
        for i, token in enumerate(tokens):
            action = ""
            
            # Если токен - число
            if isinstance(token, (int, float)):
                output.append(token)
                action = f"Число → выход"
            
            # Если токен - открывающая скобка
            elif token == '(':
                stack.push(token)
                action = f"Откр. скобка → стек"
            
            # Если токен - закрывающая скобка
            elif token == ')':
                action = "Закр. скобка - выталкиваем до '('"
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                stack.pop()  # Удаляем '('
            
            # Если токен - оператор
            elif token in '+-*/^':
                # Проверка на унарный минус
                if token == '-' and (prev_token is None or prev_token == '(' or 
                                   prev_token in '+-*/^'):
                    token = 'u-'
                    action = "Унарный минус → стек"
                else:
                    action = f"Оператор '{token}' → стек"
                
                # Выталкиваем операторы с более высоким или равным приоритетом
                while (not stack.is_empty() and 
                       stack.peek() != '(' and
                       stack.peek() in self.priority and
                       self.priority.get(stack.peek(), 0) >= self.priority[token]):
                    output.append(stack.pop())
                
                stack.push(token)
            
            # Отображаем текущее состояние
            stack_str = str(stack) if not stack.is_empty() else "[]"
            output_str = str(output) if output else "[]"
            print(f"{str(token):<10} {action:<25} {stack_str:<15} {output_str:<20}")
            
            prev_token = token
        
        # Выталкиваем оставшиеся операторы из стека
        print("-" * 60)
        print("Конец выражения - выталкиваем оставшиеся операторы:")
        while not stack.is_empty():
            op = stack.pop()
            output.append(op)
            stack_str = str(stack) if not stack.is_empty() else "[]"
            output_str = str(output) if output else "[]"
            print(f"{'':<10} {'Выталкиваем ' + str(op):<25} {stack_str:<15} {output_str:<20}")
        
        rpn_str = ' '.join(str(x) for x in output)
        print(f"\nРезультат в ОПН: {rpn_str}")
        print("=" * 50)
        return output
    
    def evaluate_rpn(self, rpn_expression):
        """Вычисляет выражение в обратной польской нотации."""
        
        print("\nШАГ 3: ВЫЧИСЛЕНИЕ ВЫРАЖЕНИЯ В ОПН")
        print("=" * 50)
        
        stack = Stack()
        
        print("\nПроцесс вычисления:")
        print("-" * 60)
        print(f"{'Токен':<10} {'Действие':<35} {'Стек':<25}")
        print("-" * 60)
        
        for token in rpn_expression:
            # Если токен - число
            if isinstance(token, (int, float)):
                stack.push(token)
                print(f"{token:<10} {'Число → стек':<35} {stack}")
            
            # Если токен - унарный минус
            elif token == 'u-':
                a = stack.pop()
                result = -a
                stack.push(result)
                print(f"{'u-':<10} {f'Унарный минус: -({a}) = {result}':<35} {stack}")
            
            # Если токен - бинарный оператор
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    result = a + b
                    action = f"{a} + {b} = {result}"
                elif token == '-':
                    result = a - b
                    action = f"{a} - {b} = {result}"
                elif token == '*':
                    result = a * b
                    action = f"{a} * {b} = {result}"
                elif token == '/':
                    if b == 0:
                        raise ValueError("Деление на ноль!")
                    result = a / b
                    action = f"{a} / {b} = {result}"
                elif token == '^':
                    result = a ** b
                    action = f"{a} ^ {b} = {result}"
                
                stack.push(result)
                print(f"{token:<10} {action:<35} {stack}")
        
        final_result = stack.pop()
        print("-" * 60)
        print(f"\nФинальный результат: {final_result}")
        print("=" * 50)
        
        return final_result
    
    def calculate(self, expression):
        """Основная функция вычисления выражения."""
        print("\n" + "=" * 70)
        print("РАБОТА КАЛЬКУЛЯТОРА")
        print("=" * 70)
        
        try:
            # Преобразование в ОПН
            rpn = self.infix_to_rpn(expression)
            
            # Вычисление результата
            result = self.evaluate_rpn(rpn)
            
            print(f"\nВЫРАЖЕНИЕ: {expression}")
            print(f"РЕЗУЛЬТАТ: {result}")
            
            return result
            
        except Exception as e:
            print(f"\nОШИБКА: {e}")
            raise


# Тестирование калькулятора
def main():
    calculator = Calculator()
    
    # Тестовые выражения
    test_expressions = [
        "3 + 4",
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "10 - 2 * 3",
        "3 + 4 * 2 / (1 - 5)",
        "-3 + 4",
        "2 ^ 3 ^ 2",
    ]
    
    print("ТЕСТИРОВАНИЕ КАЛЬКУЛЯТОРА")
    print("=" * 70)
    
    results = []
    
    for i, expr in enumerate(test_expressions, 1):
        print(f"\n{'='*40}")
        print(f"ТЕСТ {i}: {expr}")
        print(f"{'='*40}")
        
        try:
            result = calculator.calculate(expr)
            results.append((expr, result, "Успех"))
        except Exception as e:
            results.append((expr, str(e), "Ошибка"))
    
    # Сводка результатов
    print("\n" + "=" * 70)
    print("СВОДКА РЕЗУЛЬТАТОВ")
    print("=" * 70)
    print(f"{'№':<3} {'Выражение':<25} {'Результат':<20} {'Статус':<10}")
    print("-" * 70)
    
    for i, (expr, result, status) in enumerate(results, 1):
        print(f"{i:<3} {expr:<25} {str(result):<20} {status:<10}")
    
    print("=" * 70)
    
    # Объяснение алгоритма
    print("\nОБЪЯСНЕНИЕ АЛГОРИТМА")
    print("=" * 70)
    print("1. Алгоритм Дейкстры (сортировочная станция):")
    print("   - Числа сразу попадают в выходную очередь")
    print("   - Операторы помещаются в стек")
    print("   - Приоритет операторов определяет порядок выталкивания")
    print()
    print("2. Правила преобразования:")
    print("   - '(' всегда в стек")
    print("   - ')' выталкивает все до '('")
    print("   - Оператор выталкивает операторы с >= приоритетом")
    print()
    print("3. Пример для '3 + 4 * 2':")
    print("   - Токены: [3, '+', 4, '*', 2]")
    print("   - Выход: 3 4 2 * +")
    print("   - Вычисление: 3 + (4 * 2) = 11")


if __name__ == "__main__":
    main()