import random
import sympy

# Function to generate X understanding logarithms problems
def generate_understanding_logarithms_problems(X):
    problems = []
    for _ in range(X):
        base = random.randint(2, 5)
        exponent = random.randint(1, 5)
        result = sympy.log(base**exponent)
        problem = f"log_{base}({base}^{exponent})"
        problems.append((problem, result))
    return problems

# Function to generate X properties of logarithms problems
def generate_properties_logarithms_problems(X):
    problems = []
    for _ in range(X):
        base = random.randint(2, 5)
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        result = sympy.log(base**a * base**b)
        problem = f"log_{base}({base}^{a} * {base}^{b})"
        problems.append((problem, result))
    return problems

# Function to generate X solving logarithmic and exponential equations problems
def generate_solving_logarithmic_exponential_equations_problems(X):
    problems = []
    for _ in range(X):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        equation = f"{a} * e^({b}x) = {c}"
        solution = sympy.solve(equation, sympy.symbols('x'))
        problems.append((equation, solution))
    return problems

# Function to generate X applications of exponential and logarithmic functions problems
def generate_applications_exponential_logarithmic_functions_problems(X):
    problems = []
    for _ in range(X):
        population_growth_rate = random.uniform(0.01, 0.1)
        initial_population = random.randint(1000, 10000)
        time_years = random.randint(5, 20)
        final_population = initial_population * sympy.exp(population_growth_rate * time_years)
        problem = f"If a population starts with {initial_population} individuals and grows at a rate of {population_growth_rate} per year, what will be the population after {time_years} years (rounded to the nearest integer)?"
        problems.append((problem, round(final_population)))
    return problems
