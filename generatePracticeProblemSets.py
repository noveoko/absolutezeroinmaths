import random

# Import functions from previous sections
from advanced_word_problems import generate_advanced_word_problems
from advanced_equations_inequalities import generate_advanced_equations_inequalities_problems
from matrices_and_determinants import (
    generate_intro_matrices_problems,
    generate_matrix_operations_problems,
    generate_determinants_properties_problems,
    generate_solving_systems_matrices_problems,
)
from college_level_algebra import (
    generate_complex_numbers_problems,
    generate_conic_sections_problems,
    generate_polynomial_rational_functions_problems,
)

# Function to generate self-assessment quizzes for a single section
def generate_section_self_assessment_quiz(section_number, num_problems_per_section):
    quiz = []
    quiz.extend(generate_intro_matrices_problems(num_problems_per_section))
    quiz.extend(generate_complex_numbers_problems(num_problems_per_section))
    quiz.extend(generate_advanced_word_problems(num_problems_per_section))
    return {
        'section': f"Section {section_number}",
        'problems': quiz
    }

# Function to generate a full-length practice test
def generate_full_length_practice_test(num_problems_per_section):
    practice_test = []
    practice_test.extend(generate_intro_matrices_problems(num_problems_per_section))
    practice_test.extend(generate_matrix_operations_problems(num_problems_per_section))
    practice_test.extend(generate_determinants_properties_problems(num_problems_per_section))
    practice_test.extend(generate_solving_systems_matrices_problems(num_problems_per_section))
    practice_test.extend(generate_complex_numbers_problems(num_problems_per_section))
    practice_test.extend(generate_conic_sections_problems(num_problems_per_section))
    practice_test.extend(generate_polynomial_rational_functions_problems(num_problems_per_section))
    practice_test.extend(generate_advanced_equations_inequalities_problems(num_problems_per_section))
    practice_test.extend(generate_advanced_word_problems(num_problems_per_section))
    
    # Shuffle the problems to mix topics
    random.shuffle(practice_test)
    
    return practice_test

# Function to generate answer keys with explanations for exercises
def generate_answer_keys_and_explanations(problems):
    answer_key = {}
    for i, (problem, solution) in enumerate(problems, start=1):
        answer_key[f"Problem {i}"] = {
            'Problem': problem,
            'Solution': solution
        }
    return answer_key

# Function to generate practice tests and quizzes
def generate_practice_tests_and_quizzes(num_sections, num_problems_per_section):
    quizzes = [generate_section_self_assessment_quiz(i, num_problems_per_section) for i in range(1, num_sections + 1)]
    practice_test = generate_full_length_practice_test(num_problems_per_section)
    answer_keys = generate_answer_keys_and_explanations(practice_test)
    
    return {
        'Self-assessment quizzes': quizzes,
        'Full-length practice test': practice_test,
        'Answer keys and explanations': answer_keys
    }

if __name__ == "__main__":
    num_sections = 5
    num_problems_per_section = 5
    practice_materials = generate_practice_tests_and_quizzes(num_sections, num_problems_per_section)
    
    for section, quizzes in enumerate(practice_materials['Self-assessment quizzes'], start=1):
        print(f"Section {section} Self-assessment Quiz:")
        for i, (problem, solution) in enumerate(quizzes['problems'], start=1):
            print(f"Problem {i}: {problem}")
            print(f"Solution: {solution}\n")
    
    print("Full-length Practice Test:")
    for i, (problem, solution) in enumerate(practice_materials['Full-length practice test'], start=1):
        print(f"Problem {i}: {problem}")
        print(f"Solution: {solution}\n")
    
    print("Answer Keys and Explanations:")
    for problem_num, data in practice_materials['Answer keys and explanations'].items():
        print(f"{problem_num}:")
        print(f"Problem: {data['Problem']}")
        print(f"Solution: {data['Solution']}\n")
