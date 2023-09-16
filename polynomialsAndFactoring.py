import random

# Function to generate X introduction to polynomials problems
def generate_intro_polynomials_problems(X):
    problems = []
    for _ in range(X):
        degree = random.randint(1, 4)
        coefficients = [random.randint(-5, 5) for _ in range(degree + 1)]
        polynomial = " + ".join([f"{coefficients[i]}x^{degree - i}" for i in range(degree + 1)])
        problems.append((polynomial, degree))
    return problems

# Function to generate X adding and subtracting polynomials problems
def generate_add_subtract_polynomials_problems(X):
    problems = []
    for _ in range(X):
        degree1 = random.randint(1, 4)
        degree2 = random.randint(1, 4)
        coefficients1 = [random.randint(-5, 5) for _ in range(degree1 + 1)]
        coefficients2 = [random.randint(-5, 5) for _ in range(degree2 + 1)]
        polynomial1 = " + ".join([f"{coefficients1[i]}x^{degree1 - i}" for i in range(degree1 + 1)])
        polynomial2 = " + ".join([f"{coefficients2[i]}x^{degree2 - i}" for i in range(degree2 + 1)])
        operation = random.choice(['+', '-'])
        if operation == '+':
            result = [coefficients1[i] + coefficients2[i] for i in range(max(degree1, degree2) + 1)]
        else:
            result = [coefficients1[i] - coefficients2[i] for i in range(max(degree1, degree2) + 1)]
        result_polynomial = " + ".join([f"{result[i]}x^{max(degree1, degree2) - i}" for i in range(max(degree1, degree2) + 1)])
        problems.append((f"{polynomial1} {operation} {polynomial2}", result_polynomial))
    return problems

# Function to generate X multiplying and dividing polynomials problems
def generate_multiply_divide_polynomials_problems(X):
    problems = []
    for _ in range(X):
        degree1 = random.randint(1, 3)
        degree2 = random.randint(1, 3)
        coefficients1 = [random.randint(-5, 5) for _ in range(degree1 + 1)]
        coefficients2 = [random.randint(-5, 5) for _ in range(degree2 + 1)]
        polynomial1 = " + ".join([f"{coefficients1[i]}x^{degree1 - i}" for i in range(degree1 + 1)])
        polynomial2 = " + ".join([f"{coefficients2[i]}x^{degree2 - i}" for i in range(degree2 + 1)])
        operation = random.choice(['*', '/'])
        if operation == '*':
            result = [0] * (degree1 + degree2 + 1)
            for i in range(degree1 + 1):
                for j in range(degree2 + 1):
                    result[i + j] += coefficients1[i] * coefficients2[j]
            result_polynomial = " + ".join([f"{result[i]}x^{degree1 + degree2 - i}" for i in range(degree1 + degree2 + 1)])
        else:
            result = [coefficients1[i] for i in range(degree1 + 1)]
            result_polynomial = polynomial1
        problems.append((f"{polynomial1} {operation} {polynomial2}", result_polynomial))
    return problems

# Function to generate X factoring polynomials problems
def generate_factoring_polynomials_problems(X):
    problems = []
    for _ in range(X):
        degree = random.randint(2, 4)
        coefficient = random.randint(2, 5)
        roots = [random.randint(-3, 3) for _ in range(degree - 1)]
        roots_product = 1
        for root in roots:
            roots_product *= root
        constant_term = random.randint(-10, 10)
        polynomial = f"{coefficient}x^{degree}"
        for root in roots:
            polynomial += f"(x - {root})"
        if constant_term > 0:
            polynomial += f" + {constant_term}"
        elif constant_term < 0:
            polynomial += f" - {-constant_term}"
        problems.append((polynomial, roots))
    return problems
