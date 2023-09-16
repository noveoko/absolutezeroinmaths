import random

# Function to generate X introduction to functions problems
def generate_intro_functions_problems(X):
    problems = []
    for _ in range(X):
        variable = random.choice(['x', 'y', 'z'])
        equation = f"{variable} = f({variable})"
        problems.append((equation, variable))
    return problems

# Function to generate X graphing linear functions problems
def generate_graph_linear_functions_problems(X):
    problems = []
    for _ in range(X):
        slope = random.randint(-5, 5)
        intercept = random.randint(-10, 10)
        equation = f"f(x) = {slope}x + {intercept}"
        problems.append((equation, (slope, intercept)))
    return problems

# Function to generate X transformations of functions problems
def generate_transformations_functions_problems(X):
    problems = []
    for _ in range(X):
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        h = random.randint(-5, 5)
        k = random.randint(-5, 5)
        equation = f"f(x) = {a}(x - {h})^2 + {k}"
        problems.append((equation, (a, h, k)))
    return problems

# Function to generate X word problems involving functions problems
def generate_word_problems_functions(X):
    problems = []
    for _ in range(X):
        variable = random.choice(['x', 'y', 'z'])
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        h = random.randint(-5, 5)
        k = random.randint(-5, 5)
        operation = random.choice(["added to", "subtracted from"])
        if operation == "added to":
            problem = f"If you have the function f({variable}) = {a}({variable} - {h})^2 + {k}, what happens to the graph when {variable} is {operation} {h}?"
            answer = "shifts right" if h > 0 else "shifts left"
        else:
            problem = f"If you have the function f({variable}) = {a}({variable} - {h})^2 + {k}, what happens to the graph when {variable} is {operation} {h}?"
            answer = "shifts left" if h > 0 else "shifts right"
        problems.append((problem, answer))
    return problems
