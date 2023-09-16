import random

# Function to generate X single-digit addition problems
def generate_single_digit_addition_problems(X):
    problems = []
    for _ in range(X):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        problem = f"{num1} + {num2} = "
        answer = num1 + num2
        problems.append((problem, answer))
    return problems

# Function to generate X multi-digit addition problems
def generate_multi_digit_addition_problems(X, num_digits=2):
    problems = []
    for _ in range(X):
        num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        problem = f"{num1} + {num2} = "
        answer = num1 + num2
        problems.append((problem, answer))
    return problems

# Function to generate X single-digit subtraction problems
def generate_single_digit_subtraction_problems(X):
    problems = []
    for _ in range(X):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num1, num2 = max(num1, num2), min(num1, num2)  # Ensure positive results
        problem = f"{num1} - {num2} = "
        answer = num1 - num2
        problems.append((problem, answer))
    return problems

# Function to generate X multi-digit subtraction problems
def generate_multi_digit_subtraction_problems(X, num_digits=2):
    problems = []
    for _ in range(X):
        num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        num1, num2 = max(num1, num2), min(num1, num2)  # Ensure positive results
        problem = f"{num1} - {num2} = "
        answer = num1 - num2
        problems.append((problem, answer))
    return problems

# Function to generate X word problems involving addition and subtraction
def generate_word_problems_addition_subtraction(X):
    problems = []
    for _ in range(X):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operation = random.choice(["added to", "subtracted from"])
        problem = f"If you have {num1} apples and {num2} more are {operation}, how many apples do you have in total?"
        if operation == "added to":
            answer = num1 + num2
        else:
            answer = num1 - num2
        problems.append((problem, answer))
    return problems

# Function to generate X single-digit multiplication problems
def generate_single_digit_multiplication_problems(X):
    problems = []
    for _ in range(X):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        problem = f"{num1} x {num2} = "
        answer = num1 * num2
        problems.append((problem, answer))
    return problems

# Function to generate X multiplication tables practice problems
def generate_multiplication_tables_problems(X, table=2):
    problems = []
    for _ in range(X):
        num2 = random.randint(1, 10)
        problem = f"{table} x {num2} = "
        answer = table * num2
        problems.append((problem, answer))
    return problems

# Function to generate X word problems involving multiplication and division
def generate_word_problems_multiplication_division(X):
    problems = []
    for _ in range(X):
        num1 = random.randint(2, 10)
        num2 = random.randint(2, 10)
        operation = random.choice(["multiplied by", "divided by"])
        problem = f"If you have {num1 * num2} candies and you split them into {num1} equal groups, how many candies are in each group?"
        if operation == "multiplied by":
            answer = num1
        else:
            answer = num2
        problems.append((problem, answer))
    return problems
