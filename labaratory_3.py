#Output of all decimal numbers
import re


def find_multiples_of_three(input_text):
    binary = re.compile(r'\b[01]+\b')
    matches = binary.findall(input_text)

    for binary_str in matches:
        decimal = int(binary_str, 2)
        print(decimal)

# Пример использования
text = """
101
110
111
1001
1010
1100
"""
find_multiples_of_three(text)