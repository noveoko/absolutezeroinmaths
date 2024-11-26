import random
from dataclasses import dataclass
from typing import List, Tuple, Optional
import math

@dataclass
class MathProblem:
    problem: str
    solution: float
    category: str
    difficulty_score: float
    
class MathProblemGenerator:
    def __init__(self):
        self.operations = {
            'arithmetic': self._generate_arithmetic,
            'algebra': self._generate_algebra,
            'geometry': self._generate_geometry,
            'trigonometry': self._generate_trigonometry,
            'calculus': self._generate_calculus
        }
        
        # Difficulty weights for different aspects
        self.operation_weights = {
            '+': 1, '-': 1, '*': 2, '/': 3, '^': 4,
            'sqrt': 5, 'sin': 6, 'cos': 6, 'tan': 7,
            'd/dx': 8, '∫': 9
        }
        
    def generate_problem(self, min_difficulty: float = 0, max_difficulty: float = 10) -> MathProblem:
        """Generate a random math problem within specified difficulty range"""
        # Randomly select category based on difficulty range
        categories = list(self.operations.keys())
        if max_difficulty < 5:
            categories = categories[:2]  # Only arithmetic and algebra for easy problems
        elif min_difficulty > 7:
            categories = categories[3:]  # Only trig and calculus for hard problems
            
        category = random.choice(categories)
        return self.operations[category](min_difficulty, max_difficulty)
    
    def _calculate_difficulty(self, problem: str, num_operations: int, 
                            largest_number: float, decimals: bool, 
                            variables: int, category: str) -> float:
        """Calculate difficulty score based on various factors"""
        base_score = 0
        
        # Category base difficulty
        category_weights = {
            'arithmetic': 1,
            'algebra': 3,
            'geometry': 5,
            'trigonometry': 7,
            'calculus': 9
        }
        base_score += category_weights[category]
        
        # Operation complexity
        for op, weight in self.operation_weights.items():
            if op in problem:
                base_score += weight
        
        # Number of operations
        base_score += num_operations * 0.5
        
        # Size of numbers
        base_score += math.log(largest_number + 1, 10) * 0.5
        
        # Decimals and variables
        if decimals:
            base_score += 1
        base_score += variables * 1.5
        
        # Normalize to 0-10 scale
        return min(10, max(1, base_score / 3))
    
    def _generate_arithmetic(self, min_diff: float, max_diff: float) -> MathProblem:
        """Generate arithmetic problems"""
        if max_diff <= 3:  # Simple arithmetic
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            op = random.choice(['+', '-'])
            solution = a + b if op == '+' else a - b
            problem = f"{a} {op} {b}"
        elif max_diff <= 6:  # Multiple operations
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            c = random.randint(1, 50)
            op1, op2 = random.choices(['+', '-', '*'], k=2)
            problem = f"{a} {op1} {b} {op2} {c}"
            solution = eval(problem)
        else:  # Complex arithmetic
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            op = random.choice(['*', '/'])
            if op == '/':
                solution = a / b
                problem = f"{a} ÷ {b}"
            else:
                solution = a * b
                problem = f"{a} × {b}"
                
        difficulty = self._calculate_difficulty(
            problem, problem.count('+') + problem.count('-') + problem.count('*') + problem.count('/'),
            max(map(float, [num for num in problem.split() if num.isdigit()])),
            '.' in str(solution), 0, 'arithmetic'
        )
        
        return MathProblem(problem, solution, 'arithmetic', difficulty)
    
    def _generate_algebra(self, min_diff: float, max_diff: float) -> MathProblem:
        """Generate algebraic problems"""
        if max_diff <= 5:  # Simple equations
            a = random.randint(1, 10)
            b = random.randint(1, 20)
            problem = f"x + {a} = {b}"
            solution = b - a
        else:  # Quadratic equations
            a = random.randint(1, 5)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            problem = f"{a}x² + {b}x + {c} = 0"
            # Only returning one solution for simplicity
            solution = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
            
        difficulty = self._calculate_difficulty(
            problem, problem.count('+') + problem.count('-') + problem.count('^'),
            max(map(float, [num for num in problem.split() if num.replace('-','').isdigit()])),
            '.' in str(solution), 1, 'algebra'
        )
        
        return MathProblem(problem, solution, 'algebra', difficulty)
    
    def _generate_geometry(self, min_diff: float, max_diff: float) -> MathProblem:
        """Generate geometry problems"""
        if max_diff <= 6:  # Area/perimeter
            width = random.randint(1, 20)
            height = random.randint(1, 20)
            if random.choice([True, False]):
                problem = f"Find the area of a rectangle with width {width} and height {height}"
                solution = width * height
            else:
                problem = f"Find the perimeter of a rectangle with width {width} and height {height}"
                solution = 2 * (width + height)
        else:  # More complex geometry
            radius = random.randint(1, 15)
            problem = f"Find the area of a circle with radius {radius}"
            solution = math.pi * radius ** 2
            
        difficulty = self._calculate_difficulty(
            problem, 2, max(width, height), True, 0, 'geometry'
        )
        
        return MathProblem(problem, solution, 'geometry', difficulty)
    
    def _generate_trigonometry(self, min_diff: float, max_diff: float) -> MathProblem:
        """Generate trigonometry problems"""
        angle = random.choice([30, 45, 60, 90, 180, 270, 360])
        if max_diff <= 7:
            func = random.choice(['sin', 'cos'])
            problem = f"{func}({angle}°)"
            solution = math.sin(math.radians(angle)) if func == 'sin' else math.cos(math.radians(angle))
        else:
            problem = f"tan({angle}°)"
            solution = math.tan(math.radians(angle))
            
        difficulty = self._calculate_difficulty(
            problem, 1, angle, True, 0, 'trigonometry'
        )
        
        return MathProblem(problem, solution, 'trigonometry', difficulty)
    
    def _generate_calculus(self, min_diff: float, max_diff: float) -> MathProblem:
        """Generate calculus problems"""
        if max_diff <= 8:  # Basic derivatives
            a = random.randint(1, 5)
            n = random.randint(2, 4)
            problem = f"Find d/dx of {a}x^{n}"
            solution = a * n  # Coefficient of x^(n-1)
        else:  # More complex derivatives
            a = random.randint(1, 3)
            problem = f"Find d/dx of sin({a}x)"
            solution = a  # Coefficient of cos(ax)
            
        difficulty = self._calculate_difficulty(
            problem, 2, max(a, n), False, 1, 'calculus'
        )
        
        return MathProblem(problem, solution, 'calculus', difficulty)
    
    def generate_problem_set(self, num_problems: int, 
                           min_difficulty: float = 0, 
                           max_difficulty: float = 10) -> List[MathProblem]:
        """Generate a set of problems and sort them by difficulty"""
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(min_difficulty, max_difficulty)
            problems.append(problem)
            
        # Sort by difficulty score
        return sorted(problems, key=lambda x: x.difficulty_score)

# Example usage
generator = MathProblemGenerator()

# Generate 10 problems with increasing difficulty
problems = generator.generate_problem_set(10, min_difficulty=1, max_difficulty=10)

# Print problems with their difficulty scores
for i, p in enumerate(problems, 1):
    print(f"\nProblem {i}:")
    print(f"Category: {p.category}")
    print(f"Problem: {p.problem}")
    print(f"Solution: {p.solution:.2f}")
    print(f"Difficulty: {p.difficulty_score:.2f}/10")