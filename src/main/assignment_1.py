import math

def approximation_algorithm(x, tol=1e-6):
    """
    Approximate the square root of x using an iterative approach (from Ch2.1, Slide 11).
    """
    guess = x / 2.0
    while abs(guess * guess - x) > tol:
        guess = (guess + x / guess) / 2.0
    return guess

def bisection_method(f, a, b, tol=1e-6):
    """
    Find the root of function f using the Bisection Method (from Ch2.1, Slide 14).
    """
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at a and b.")
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    """
    Fixed-Point Iteration method (from Ch2.2, Slide 13).
    """
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Fixed-point iteration did not converge.")

def newton_raphson_method(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method for finding roots (from Ch2.3, Slide 7).
    """
    x = x0
    for _ in range(max_iter):
        f_x = f(x)
        df_x = df(x)
        if df_x == 0:
            raise ValueError("Derivative is zero, method fails.")
        x_new = x - f_x / df_x
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Newton-Raphson did not converge.")

# Example usage
def example_functions():
    print("Approximation Algorithm (sqrt(10)):", approximation_algorithm(10))
    print("Bisection Method (root of x^2 - 4 in [1, 3]):", bisection_method(lambda x: x**2 - 4, 1, 3))
    print("Fixed-Point Iteration (g(x) = cos(x), x0=1):", fixed_point_iteration(math.cos, 1))
    print("Newton-Raphson (root of x^2 - 4, x0=2):", newton_raphson_method(lambda x: x**2 - 4, lambda x: 2*x, 2))

if __name__ == "__main__":
    example_functions()
