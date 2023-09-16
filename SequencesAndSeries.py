import random
import sympy

# Function to generate X introduction to sequences and series problems
def generate_intro_sequences_series_problems(X):
    problems = []
    for _ in range(X):
        sequence = [random.randint(1, 10) for _ in range(5)]
        problem = f"Find the next term in the sequence: {', '.join(map(str, sequence))}, ..."
        problems.append((problem, sequence[-1] + random.randint(1, 5)))
    return problems

# Function to generate X arithmetic sequences and series problems
def generate_arithmetic_sequences_series_problems(X):
    problems = []
    for _ in range(X):
        common_diff = random.randint(1, 5)
        first_term = random.randint(1, 10)
        n = random.randint(5, 10)
        nth_term = first_term + (n - 1) * common_diff
        sum_series = n * (first_term + nth_term) // 2
        problem1 = f"Find the {n}-th term of the arithmetic sequence: {first_term}, {first_term + common_diff}, ..."
        problem2 = f"Find the sum of the first {n} terms of the sequence."
        problems.append((problem1, nth_term))
        problems.append((problem2, sum_series))
    return problems

# Function to generate X geometric sequences and series problems
def generate_geometric_sequences_series_problems(X):
    problems = []
    for _ in range(X):
        common_ratio = random.uniform(1.1, 2.0)
        first_term = random.randint(1, 5)
        n = random.randint(4, 8)
        nth_term = first_term * (common_ratio ** (n - 1))
        sum_series = first_term * (1 - common_ratio**n) / (1 - common_ratio)
        problem1 = f"Find the {n}-th term of the geometric sequence: {first_term}, {first_term * common_ratio}, ..."
        problem2 = f"Find the sum of the first {n} terms of the sequence."
        problems.append((problem1, nth_term))
        problems.append((problem2, sum_series))
    return problems

# Function to generate X word problems involving sequences and series problems
def generate_word_problems_sequences_series(X):
    problems = []
    for _ in range(X):
        n = random.randint(5, 10)
        first_term = random.randint(1, 5)
        common_diff = random.randint(1, 5)
        nth_term = first_term + (n - 1) * common_diff
        sum_series = n * (first_term + nth_term) // 2
        problem1 = f"In an arithmetic sequence, the {n}-th term is {nth_term}. What is the first term if the common difference is {common_diff}?"
        problem2 = f"What is the sum of the first {n} terms of an arithmetic sequence with the first term {first_term} and a common difference of {common_diff}?"
        problems.append((problem1, first_term))
        problems.append((problem2, sum_series))

    return problems
