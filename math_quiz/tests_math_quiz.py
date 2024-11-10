import unittest
from math_quiz import generate_random_number, generate_random_operator, calculate_result


class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if the generated number is within the specified range
        min_value = 1
        max_value = 10
        random_number = generate_random_number(min_value, max_value)
        self.assertTrue(min_value <= random_number <= max_value)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of the allowed operators
        allowed_operators = {'+', '-', '*'}
        random_operator = generate_random_operator()
        self.assertIn(random_operator, allowed_operators)

    def test_calculate_result(self):
        # Test the correctness of the calculated result for each operator
        test_cases = [
            {'number1': 5, 'number2': 3, 'operator': '+', 'expected_result': 8},
            {'number1': 5, 'number2': 3, 'operator': '-', 'expected_result': 2},
            {'number1': 5, 'number2': 3, 'operator': '*', 'expected_result': 15},
        ]

        for case in test_cases:
            with self.subTest(case=case):
                problem, result = calculate_result(case['number1'], case['number2'], case['operator'])
                self.assertEqual(result, case['expected_result'])
                self.assertEqual(problem, f"{case['number1']} {case['operator']} {case['number2']}")


if __name__ == '__main__':
    unittest.main()
