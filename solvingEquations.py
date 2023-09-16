import random

# Function to generate X introduction to equations problems
def generate_intro_equations_problems(X):
    problems = []
    for _ in range(X):
        variable = random.choice(['x', 'y', 'z'])
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        problem = f"{num1}{variable} + {num2} = {num1 + num2}"
        problems.append((problem, variable))
    return problems

# Function to generate X linear equations with one variable problems
def generate_linear_equations_one_variable_problems(X):
    problems = []
    for _ in range(X):
        variable = random.choice(['x', 'y', 'z'])
        coefficient = random.randint(2, 9)
        constant = random.randint(1, 10)
        problem = f"{coefficient}{variable} - {constant} = {coefficient * variable - constant}"
        problems.append((problem, variable))
    return problems

# Function to generate X word problems involving linear equations
def generate_word_problems_linear_equations(X):
    problems = []
    for _ in range(X):
        variable = random.choice(['x', 'y', 'z'])
        coefficient = random.randint(2, 5)
        constant = random.randint(5, 15)
        value = random.randint(1, 10)
        operation = random.choice(["added to", "subtracted from"])
        if operation == "added to":
            problem = f"{coefficient}{variable} + {constant} = {value + coefficient * constant}"
        else:
            problem = f"{coefficient}{variable} - {constant} = {value - coefficient * constant}"
        problems.append((problem, variable))
    return problems

# Function to generate X systems of linear equations problems
def generate_systems_linear_equations_problems(X):
    problems = []
    for _ in range(X):
        variables = ['x', 'y', 'z']
        coefficients = [random.randint(1, 5) for _ in range(3)]
        constants = [random.randint(1, 10) for _ in range(3)]
        equations = [f"{coefficients[i]}{variables[i]} + {constants[i]}" for i in range(3)]
        solution = [constants[i] / coefficients[i] for i in range(3)]
        problem = f"System of Equations:\n{equations[0]} = {solution[0]}\n{equations[1]} = {solution[1]}\n{equations[2]} = {solution[2]}"
        problems.append((problem, solution))
    return problems

# Function to generate X word problems involving systems of linear equations
def generate_word_problems_systems_equations(X):
    problems = []
    for _ in range(X):
        variables = ['x', 'y']
        coefficients = [random.randint(2, 5) for _ in range(2)]
        constants = [random.randint(5, 10) for _ in range(2)]
        values = [random.randint(1, 10) for _ in range(2)]
        operation1 = random.choice(["added to", "subtracted from"])
        operation2 = random.choice(["added to", "subtracted from"])
        if operation1 == "added to":
            equation1 = f"{coefficients[0]}{variables[0]} + {constants[0]} = {values[0] + coefficients[0] * constants[0]}"
        else:
            equation1 = f"{coefficients[0]}{variables[0]} - {constants[0]} = {values[0] - coefficients[0] * constants[0]}"
        if operation2 == "added to":
            equation2 = f"{coefficients[1]}{variables[1]} + {constants[1]} = {values[1] + coefficients[1] * constants[1]}"
        else:
            equation2 = f"{coefficients[1]}{variables[1]} - {constants[1]} = {values[1] - coefficients[1] * constants[1]}"
        problem = f"Solve the following system of equations:\n{equation1}\n{equation2}"
        solutions = [values[0], values[1]]
        problems.append((problem, solutions))
    return problems
