import random
import sympy

# Function to generate X introduction to matrices problems
def generate_intro_matrices_problems(X):
    problems = []
    for _ in range(X):
        rows = random.randint(2, 4)
        cols = random.randint(2, 4)
        matrix = [[random.randint(1, 5) for _ in range(cols)] for _ in range(rows)]
        problem = f"Write a {rows}x{cols} matrix."
        problems.append((problem, matrix))
    return problems

# Function to generate X matrix operations (addition, multiplication) problems
def generate_matrix_operations_problems(X):
    problems = []
    for _ in range(X):
        rows = random.randint(2, 4)
        cols = random.randint(2, 4)
        matrix1 = [[random.randint(1, 5) for _ in range(cols)] for _ in range(rows)]
        matrix2 = [[random.randint(1, 5) for _ in range(cols)] for _ in range(rows)]
        operation = random.choice(['+', '*'])
        if operation == '+':
            result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
            problem = f"Perform matrix addition: \nMatrix 1:\n{matrix1}\nMatrix 2:\n{matrix2}"
        else:
            result = sympy.Matrix(matrix1) * sympy.Matrix(matrix2)
            problem = f"Perform matrix multiplication: \nMatrix 1:\n{matrix1}\nMatrix 2:\n{matrix2}"
        problems.append((problem, result.tolist()))
    return problems

# Function to generate X determinants and their properties problems
def generate_determinants_properties_problems(X):
    problems = []
    for _ in range(X):
        order = random.randint(2, 4)
        matrix = sympy.Matrix([[random.randint(1, 5) for _ in range(order)] for _ in range(order)])
        determinant = matrix.det()
        problem = f"Find the determinant of the following {order}x{order} matrix:\n{matrix}"
        problems.append((problem, determinant))
    return problems

# Function to generate X solving systems of linear equations using matrices problems
def generate_solving_systems_matrices_problems(X):
    problems = []
    for _ in range(X):
        num_equations = random.randint(2, 3)
        num_variables = random.randint(2, 3)
        coefficients = [[random.randint(-5, 5) for _ in range(num_variables)] for _ in range(num_equations)]
        constants = [random.randint(-10, 10) for _ in range(num_equations)]
        augmented_matrix = sympy.Matrix(coefficients + [constants])
        solutions = sympy.solve_linear_system(augmented_matrix, sympy.symbols('x0 x1 x2'))
        problem = "Solve the following system of equations using matrices:\n"
        for i in range(num_equations):
            equation = " + ".join([f"{coefficients[i][j]}x{j}" for j in range(num_variables)])
            problem += f"{equation} = {constants[i]}\n"
        problems.append((problem, solutions))
    return problems
