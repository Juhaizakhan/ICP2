
# Online Python - IDE, Editor, Compiler, Interpreter

def count_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
input_string = 'The quick Brow Fox'
upper_count, lower_count = count_case(input_string)
print("No. of Upper-case characters:", upper_count)
print("No. of Lower-case Characters:", lower_count)
