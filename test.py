import unittest
import Number1


class TestTypeTriangle(unittest.TestCase):

    # Равносторонний
    def test_equilateralTriange(self):
        # Тестирование разлчиных вариантов значений

        # Тестирование на корректный ввод
        self.assertTrue(Number1.equilateralTriange(12, 12, 12), True)

        # Тестирование на некорректный ввод данных
        self.assertFalse(Number1.equilateralTriange(16, 16, 0), False)
        self.assertFalse(Number1.equilateralTriange(7, 0, 7), False)
        self.assertFalse(Number1.equilateralTriange(0, 1, 1), False)

        # Эквивалентное
        # Тестирование целочисленные
        self.assertFalse(Number1.equilateralTriange(-5, 0, 15), False)

        # Тестирование специального ввода специального символа
        self.assertFalse(Number1.equilateralTriange('@', 12, 13), False)

        # Тестирование ввода символов
        self.assertFalse(Number1.equilateralTriange('a', 'b', 'c'), False)

        # Граничное
        # Граничное нижней границы и верхней
        self.assertFalse(Number1.equilateralTriange(-2147483648, 0, 2147483647), False)

        # Тестирование вернхней границы
        self.assertFalse(Number1.equilateralTriange(2147483646, 2147483647, 2147483648), False)

        # Тестирование нижней гранциы
        self.assertFalse(Number1.equilateralTriange(-21474836468, -2147483647, -2147483646), False)

    # Разносторонний
    def test_versatileTriangle(self):
        # Тестирование на корректный ввод
        self.assertTrue(Number1.versatileTriangle(13, 10, 11), True)

        # Тестирование на некорректный ввод данных
        self.assertFalse(Number1.versatileTriangle(12, 12, 0), False)
        self.assertFalse(Number1.versatileTriangle(0, 19, 19), False)

        # Эквивалентное по типу значения отрицательноое,
        # Тестирование целочисленные
        self.assertTrue(Number1.versatileTriangle(-1, 0, 1), False)

        # Тестирование специального ввода специального символа
        self.assertTrue(Number1.versatileTriangle('@', 12, 13), False)

        # Тестирование ввода символов
        self.assertTrue(Number1.versatileTriangle('a', 'b', 'c'), False)

        # Граничное
        # Граничное нижней границы и верхней
        self.assertTrue(Number1.versatileTriangle(-2147483648, 0, 2147483647), False)
        # Граниченое тестирование по верхней границе
        self.assertTrue(Number1.versatileTriangle(2147483646, 2147483647, 2147483648), False)
        # Граниченое тестирование по нижней границе
        self.assertTrue(Number1.versatileTriangle(-21474836468, -2147483647, -2147483646), False)

    # Равнобедренный
    def test_isoscelesTriangle(self):
        # Тестирование на корркетный ввод
        self.assertTrue(Number1.isoscelesTriangle(12, 12, 6), True)
        self.assertTrue(Number1.isoscelesTriangle(15, 9, 15), True)
        self.assertTrue(Number1.isoscelesTriangle(3, 9, 9), True)

        # Тестирование на некорректный ввод данных
        self.assertFalse(Number1.isoscelesTriangle(6, 10, 12), False)
        self.assertFalse(Number1.isoscelesTriangle(7, 13, 12), False)
        self.assertFalse(Number1.isoscelesTriangle(19, 14, 20), False)
        self.assertFalse(Number1.isoscelesTriangle(6, 7, 1), False)
        self.assertFalse(Number1.isoscelesTriangle(12, 6, 11), False)
        self.assertFalse(Number1.isoscelesTriangle(22, 21, 16), False)

        # Эквивалентное 
        # Тестирование целочисленные
        self.assertFalse(Number1.isoscelesTriangle(-5, 0, 15), False)
        # Тестирование специального ввода специального символа
        self.assertFalse(Number1.isoscelesTriangle('@', 12, 13), False)
        # Тестирование ввода символов
        self.assertFalse(Number1.isoscelesTriangle('a', 'b', 'c'), False)

        # Граничное
        # Граничное нижней границы до верхней
        self.assertFalse(Number1.isoscelesTriangle(-2147483648, 0, 2147483647), False)
        # Тестирование верхней гранциы
        # Тестирование нижней гранциы
        self.assertFalse(Number1.isoscelesTriangle(-21474836468, -2147483647, -2147483646), False)

    #Проверка на существование треугольника
    def test_checkNumber(self):
        # Тестирование на корркетный ввод данных
        self.assertTrue(Number1.checkNumber(1, 2, 3), True)
        self.assertTrue(Number1.checkNumber(1, 3, 2), True)
        self.assertTrue(Number1.checkNumber(3, 1, 2), True)
        self.assertTrue(Number1.checkNumber(3, 2, 1), True)
        self.assertTrue(Number1.checkNumber(2, 1, 3), True)
        self.assertTrue(Number1.checkNumber(2, 3, 1), True)

        # Тестирование на некорректный ввод данных
        self.assertFalse(Number1.checkNumber(3, 1, 0), False)
        self.assertFalse(Number1.checkNumber(4, 0, 2), False)
        self.assertFalse(Number1.checkNumber(0, 3, 1), False)

        # Эквивалентное 
        # Тестирование целочисленные
        self.assertFalse(Number1.checkNumber(-5, 0, 15), False)

        # Граничное
        # Граничное нижней границы до верхней
        self.assertFalse(Number1.checkNumber(-2147483648, 0, 2147483647), False)


if __name__ == "__main__":
    unittest.main()
