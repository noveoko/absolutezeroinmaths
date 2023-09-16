import random
import sympy

# Function to generate X understanding quadratic equations problems
def generate_understanding_quadratic_equations_problems(X):
    problems = []
    for _ in range(X):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        equation = f"{a}x^2 + {b}x + {c} = 0"
        problems.append((equation, (a, b, c)))
    return problems

# Function to generate X solving quadratic equations by factoring problems
def generate_solving_quadratic_by_factoring_problems(X):
    problems = []
    for _ in range(X):
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        root1 = sympy.Rational(-b + sympy.sqrt(b**2 - 4*a*c), 2*a)
        root2 = sympy.Rational(-b - sympy.sqrt(b**2 - 4*a*c), 2*a)
        equation = f"{a}x^2 + {b}x + {c} = 0"
        problems.append((equation, (root1, root2)))
    return problems

# Function to generate X quadratic formula and its applications problems
def generate_quadratic_formula_problems(X):
    problems = []
    for _ in range(X):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        root1 = sympy.Rational(-b + sympy.sqrt(b**2 - 4*a*c), 2*a)
        root2 = sympy.Rational(-b - sympy.sqrt(b**2 - 4*a*c), 2*a)
        equation = f"{a}x^2 + {b}x + {c} = 0"
        problems.append((equation, (root1, root2)))
    return problems

# Function to generate X word problems involving quadratic equations
def generate_word_problems_quadratic_equations(X):
    problems = []
    for _ in range(X):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        equation = f"{a}x^2 + {b}x + {c} = 0"
        solutions = sympy.solve(equation, sympy.symbols('x'))
        if solutions[0] == solutions[1]:
            problem = f"The roots of the quadratic equation {equation} are equal. What is their value?"
            answer = solutions[0]
        else:
            problem = f"The roots of the quadratic equation {equation} are distinct. Find their values."
            answer = solutions
        problems.append((problem, answer))
    return problems
