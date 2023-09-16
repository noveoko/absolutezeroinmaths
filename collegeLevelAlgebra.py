import random
import sympy

# Function to generate X complex numbers problems
def generate_complex_numbers_problems(X):
    problems = []
    for _ in range(X):
        real_part = random.randint(-5, 5)
        imaginary_part = random.randint(-5, 5)
        complex_number = sympy.Rational(real_part) + sympy.I * sympy.Rational(imaginary_part)
        problem = f"Simplify the complex number: {real_part} + {imaginary_part}i"
        problems.append((problem, complex_number))
    return problems

# Function to generate X conic sections problems
def generate_conic_sections_problems(X):
    problems = []
    for _ in range(X):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        h = random.randint(-5, 5)
        k = random.randint(-5, 5)
        equation = f"{a}(x - {h})^2 + {b}(y - {k})^2 = 1"
        problems.append((equation, (a, b, h, k)))
    return problems

# Function to generate X polynomial and rational functions problems
def generate_polynomial_rational_functions_problems(X):
    problems = []
    for _ in range(X):
        degree = random.randint(2, 4)
        coefficients = [random.randint(-5, 5) for _ in range(degree + 1)]
        polynomial = " + ".join([f"{coefficients[i]}x^{degree - i}" for i in range(degree + 1)])
        problem = f"Simplify the polynomial: {polynomial}"
        problems.append((problem, coefficients))
    return problems

import random
import sympy

# Function to generate X advanced topics in equations and inequalities problems
def generate_advanced_equations_inequalities_problems(X):
    problems = []
    for _ in range(X):
        problem_type = random.choice(['equation', 'inequality'])
        
        if problem_type == 'equation':
            # Generate advanced equation problems
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            equation = f"{a}x^2 + {b}x + {c} = 0"
            solutions = sympy.solve(equation, sympy.symbols('x'))
            problems.append((equation, solutions))
        
        elif problem_type == 'inequality':
            # Generate advanced inequality problems
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            inequality = f"{a}x + {b} > 0"
            solutions = sympy.solve_univariate_inequality(inequality, sympy.symbols('x'), relational=False)
            problems.append((inequality, solutions))

    return problems


import random
import sympy

# Function to generate X advanced word problems problems
def generate_advanced_word_problems(X):
    problems = []
    for _ in range(X):
        problem_type = random.choice(['profit', 'interest', 'optimization'])
        
        if problem_type == 'profit':
            # Generate advanced profit maximization problem
            cost_function = f"C(x) = {random.randint(1, 5)}x + {random.randint(1, 5)}"
            revenue_function = f"R(x) = {random.randint(5, 10)}x"
            problem = f"A company produces and sells x units of a product. The cost function is {cost_function}, and the revenue function is {revenue_function}. Find the profit-maximizing quantity of x."
            problems.append((problem, sympy.solve(sympy.Eq(sympy.diff(f"R(x) - C(x)", sympy.symbols('x')), 0), sympy.symbols('x'))))
        
        elif problem_type == 'interest':
            # Generate advanced interest rate problem
            principal = random.randint(1000, 5000)
            rate = random.uniform(0.05, 0.1)
            time = random.randint(5, 10)
            problem = f"A principal amount of ${principal} is invested at an annual interest rate of {rate * 100}%. How much money will be in the account after {time} years?"
            future_value = principal * (1 + rate) ** time
            problems.append((problem, round(future_value, 2)))

        elif problem_type == 'optimization':
            # Generate advanced optimization problem
            objective_function = f"f(x) = {random.randint(1, 5)}x^2 + {random.randint(1, 5)}x + {random.randint(1, 5)}"
            problem = f"Find the minimum value of the function {objective_function} over the interval [a, b], where a = {random.randint(-5, 0)} and b = {random.randint(1, 5)}."
            problems.append((problem, sympy.solve(sympy.Eq(sympy.diff(objective_function, sympy.symbols('x')), 0), sympy.symbols('x'))))

    return problems

