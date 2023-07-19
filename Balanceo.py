def is_balanced(expression):
    stack = []
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) == 0 or pairs[stack[-1]] != char:
                return False
            stack.pop()

    return len(stack) == 0


file_path = "C:/Users/gsant/Desktop/TeoriaComputacion/Lab2/dataEjercicio2.txt"  # Path to the text file

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        expression = line.strip()  # Remove leading/trailing whitespaces and newlines

        if is_balanced(expression):
            print(f"The expression '{expression}' is balanced.")
        else:
            print(f"The expression '{expression}' is not balanced.")
