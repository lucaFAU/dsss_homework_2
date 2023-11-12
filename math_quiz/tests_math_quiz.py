import unittest
from math_quiz import get_random_int, get_random_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"get_random_int failed: number {rand_num} is out of intervall")


    def test_function_B(self):
        # Test if the choosen number is one from the intervall
        for _ in range(1000):
            rand_op = get_random_operator()
            self.assertIn(rand_op, ['+', '-', '*'], f"get_random_operator failed: operator {rand_op} is not in intervall")

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (1, 3, '+', '1 + 3', 4),
                (5, 2, '-', '5 - 2', 3),
                (1, 3, '-', '1 - 3', -2),
                (5, 2, '*', '5 * 2', 10),
                (1, 3, '*', '1 * 3', 3),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                p, a = perform_operation(num1, num2, operator)
                print(p)
                print(expected_problem)
                print(f"perform_operation failed: operation string is {p} but {expected_problem} is expected")
                self.assertTrue(p, expected_problem, "perform_operation failed: operation string is not as expected")
                self.assertTrue(a, expected_answer, "perform_operation failed: result is not as expected")

if __name__ == "__main__":
    unittest.main()
