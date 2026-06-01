import unittest
from mysum import my_sum

# Run with:  python test_mysum.py -v

class TestMySum(unittest.TestCase):

    # --- carried over from v2 (all pass now) ---

    def test_list_of_integers(self):
        # Arrange
        numbers = [1, 2, 3]
        # Act
        result = my_sum(numbers)
        # Assert
        self.assertEqual(result, 6)

    def test_tuple_of_integers(self):
        # Arrange
        numbers = (10, 20, 30)
        # Act
        result = my_sum(numbers)
        # Assert
        self.assertEqual(result, 60)

    def test_empty_list(self):
        # Arrange
        numbers = []
        # Act
        result = my_sum(numbers)
        # Assert
        self.assertEqual(result, 0)

    def test_bool_argument(self):
        result = my_sum(True)
        self.assertEqual(result, None)

    def test_mixed_list(self):
        # Fixed in v3: element check catches the string → returns None
        numbers = [1, "hello", 3]
        result = my_sum(numbers)
        self.assertEqual(result, None)

    # --- new tests for v3 ---

    def test_list_of_floats(self):
        # Arrange
        numbers = [1.5, 2.5, 3.0]
        # Act
        result = my_sum(numbers)
        # Assert
        self.assertAlmostEqual(result, 7.0)

    def test_mixed_int_float(self):
        # Arrange — ints and floats together should work
        numbers = [1, 2.5, 3]
        # Act
        result = my_sum(numbers)
        # Assert
        self.assertAlmostEqual(result, 6.5)


if __name__ == '__main__':
    unittest.main()
