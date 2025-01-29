import unittest
from src.main.assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson_method
import math

class TestNumericalMethods(unittest.TestCase):
    
    def test_approximation_algorithm(self):
        self.assertAlmostEqual(approximation_algorithm(9), 3, places=5)
        self.assertAlmostEqual(approximation_algorithm(2), math.sqrt(2), places=5)
    
    def test_bisection_method(self):
        self.assertAlmostEqual(bisection_method(lambda x: x**2 - 4, 1, 3), 2, places=5)
        self.assertAlmostEqual(bisection_method(lambda x: x**3 - 27, 2, 4), 3, places=5)
        with self.assertRaises(ValueError):
            bisection_method(lambda x: x**2 + 1, -1, 1)
    
    def test_fixed_point_iteration(self):
        self.assertAlmostEqual(fixed_point_iteration(math.cos, 1), 0.739085, places=5)
        with self.assertRaises(ValueError):
            fixed_point_iteration(lambda x: x + 1, 1)
    
    def test_newton_raphson_method(self):
        self.assertAlmostEqual(newton_raphson_method(lambda x: x**2 - 4, lambda x: 2*x, 2), 2, places=5)
        self.assertAlmostEqual(newton_raphson_method(lambda x: x**3 - 8, lambda x: 3*x**2, 2), 2, places=5)
        with self.assertRaises(ValueError):
            newton_raphson_method(lambda x: x**2 - 4, lambda x: 0, 2)
    
if __name__ == "__main__":
    unittest.main()
