import re


def multiplicity_3(binary_str):

    pattern = re.findall(r'^(1(01*0)*1|0)+$',binary_str)

    return bool(pattern)


# Пример использования
binary_numbers_str = "10 11 110 1101 1010 1001 1111 10101 1100 010110 111001 101011 001100 111100 010101 110011 100110 000111 011010"
binary_numbers = binary_numbers_str.split()

for binary_number in binary_numbers:
    if multiplicity_3(binary_number):
        print(f"{binary_number} делится на 3 в двоичной системе.")

