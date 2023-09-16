import random
import sympy

# Function to generate X introduction to rational expressions problems
def generate_intro_rational_expressions_problems(X):
    problems = []
    for _ in range(X):
        numerator = random.randint(1, 5)
        denominator = random.randint(2, 5)
        expression = sympy.Rational(numerator, denominator)
        problems.append((expression, (numerator, denominator)))
    return problems

# Function to generate X simplifying rational expressions problems
def generate_simplify_rational_expressions_problems(X):
    problems = []
    for _ in range(X):
        num1 = random.randint(1, 5)
        den1 = random.randint(2, 5)
        num2 = random.randint(1, 5)
        den2 = random.randint(2, 5)
        expression = sympy.Rational(num1, den1) + sympy.Rational(num2, den2)
        problems.append((expression, (num1, den1, num2, den2)))
    return problems

# Function to generate X solving rational equations problems
def generate_solving_rational_equations_problems(X):
    problems = []
    for _ in range(X):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)
        equation = f"{a}/{b}x + {c}/{d} = 0"
        solutions = [sympy.Rational(-c/d, a/b)]
        problems.append((equation, solutions))
    return problems

# Function to generate X word problems involving rational expressions problems
def generate_word_problems_rational_expressions(X):
    problems = []
    for _ in range(X):
        num1 = random.randint(1, 5)
        den1 = random.randint(2, 5)
        num2 = random.randint(1, 5)
        den2 = random.randint(2, 5)
        operation = random.choice(["added to", "subtracted from"])
        if operation == "added to":
            expression = sympy.Rational(num1, den1) + sympy.Rational(num2, den2)
            problem = f"If you add {num1}/{den1} and {num2}/{den2}, what is the result?"
        else:
            expression = sympy.Rational(num1, den1) - sympy.Rational(num2, den2)
            problem = f"If you subtract {num2}/{den2} from {num1}/{den1}, what is the result?"
        problems.append((problem, expression))
    return problems
