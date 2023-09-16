import random

# Function to generate X understanding inequalities problems
def generate_understanding_inequalities_problems(X):
    problems = []
    for _ in range(X):
        variable = random.choice(['x', 'y', 'z'])
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        comparison = random.choice(['<', '>', '<=', '>='])
        problem = f"{num1}{variable} {comparison} {num2}"
        problems.append((problem, comparison))
    return problems

# Function to generate X solving linear inequalities problems
def generate_solving_linear_inequalities_problems(X):
    problems = []
    for _ in range(X):
        variable = random.choice(['x', 'y', 'z'])
        coefficient = random.randint(2, 9)
        constant = random.randint(1, 10)
        inequality = random.choice(['<', '>', '<=', '>='])
        problem = f"{coefficient}{variable} {inequality} {coefficient * variable} - {constant}"
        problems.append((problem, inequality))
    return problems

# Function to generate X word problems involving inequalities
def generate_word_problems_inequalities(X):
    problems = []
    for _ in range(X):
        variable = random.choice(['x', 'y', 'z'])
        coefficient = random.randint(2, 5)
        constant = random.randint(5, 15)
        value = random.randint(1, 10)
        operation = random.choice(["added to", "subtracted from"])
        inequality = random.choice(['<', '>', '<=', '>='])
        if operation == "added to":
            problem = f"If you have {coefficient * value} {variable} and {constant} more are {operation}, how does the inequality look like?"
        else:
            problem = f"If you have {coefficient * value} {variable} and {constant} are {operation}, how does the inequality look like?"
        problems.append((problem, inequality))
    return problems
