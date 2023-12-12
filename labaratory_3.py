import re


def find_multiples_of_three(input_text):
    binary = re.compile(r'\b[01]+\b')
    matches = binary.findall(input_text)

    for binary_str in matches:

        decimal = int(binary_str, 2)
        if decimal % 3 == 0:
            print(binary_str)


# Пример использования
text = """
101
110
111
1001
1010
1100
"""
print("Строки с двоичной записью числа, кратного 3:")
find_multiples_of_three(text)