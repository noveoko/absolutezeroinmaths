import random
import sympy

# Function to generate X understanding exponents problems
def generate_understanding_exponents_problems(X):
    problems = []
    for _ in range(X):
        base = random.randint(2, 5)
        exponent = random.randint(1, 5)
        problem = f"{base}^{exponent}"
        problems.append((problem, base**exponent))
    return problems

# Function to generate X exponential operations problems
def generate_exponential_operations_problems(X):
    problems = []
    for _ in range(X):
        base1 = random.randint(2, 5)
        exponent1 = random.randint(1, 5)
        base2 = random.randint(2, 5)
        exponent2 = random.randint(1, 5)
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '+':
            result = base1**exponent1 + base2**exponent2
        elif operation == '-':
            result = base1**exponent1 - base2**exponent2
        elif operation == '*':
            result = base1**exponent1 * base2**exponent2
        else:
            result = sympy.Rational(base1**exponent1, base2**exponent2)
        problem = f"{base1}^{exponent1} {operation} {base2}^{exponent2}"
        problems.append((problem, result))
    return problems

# Function to generate X introduction to radicals problems
def generate_intro_radicals_problems(X):
    problems = []
    for _ in range(X):
        root = random.randint(2, 4)
        radicand = random.randint(1, 10)
        problem = f"√{radicand} (root {root})"
        problems.append((problem, radicand**(1/root)))
    return problems

# Function to generate X simplifying radicals problems
def generate_simplify_radicals_problems(X):
    problems = []
    for _ in range(X):
        root = random.randint(2, 4)
        radicand = random.randint(1, 10)
        simplified = sympy.root(radicand, root)
        problem = f"√{radicand} (root {root})"
        problems.append((problem, simplified))
    return problems

# Function to generate X solving equations with exponents and radicals problems
def generate_solving_exponents_radicals_problems(X):
    problems = []
    for _ in range(X):
        base = random.randint(2, 5)
        exponent = random.randint(2, 4)
        equation = f"{base}^x = {base**(exponent)}"
        problems.append((equation, exponent))
    return problems
