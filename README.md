# Unittest-TriangleType
Юнит тест на Python для приложения, определяющего тип треугольника.

Разработка программы на Python.
Даны длины сторон треугольника, определить вид треугольника и его площадь. 
Выполнить контроль вводимых чисел.
1. Остроугольный треугольник
2. Тупоугольный треугольник
3. Прямоугольный треугольник
Ограничения:
- три числа не могут быть определены как стороны треугольника, - если хотя бы одно из них меньше или равно 0;
- сумма двух из них меньше третьего.
Подготовить набор тестовых вариантов для обнаружения ошибок в программе и оформить результат.

Программа тестирует 4 основных функции программы:
1.  # Равносторонний
    def test_equilateralTriange(self):
    
2. # Разносторонний
    def test_versatileTriangle(self):
    
3. # Равнобедренный
    def test_isoscelesTriangle(self):
    
4. #Проверка на существование треугольника 
    def test_checkNumber(self):
