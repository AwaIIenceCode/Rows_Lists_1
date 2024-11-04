def math_calculating():
    math_expression = input('Enter a mathematical expression\n> ')

    if "+" in math_expression:
        numbers_after = math_expression.split("+")
        operator = "+"
    elif "-" in math_expression:
        numbers_after = math_expression.split("-")
        operator = "-"
    elif "/" in math_expression:
        numbers_after = math_expression.split("/")
        operator = "/"
    elif "*" in math_expression:
        numbers_after = math_expression.split("*")
        operator = "*"
    else:
        print("this kind of action hasn't been brought to you by the developers yet xD")

    num_1 = float(numbers_after[0])
    num_2 = float(numbers_after[1])
    try:
        if operator == "+":
            result = num_1 + num_2
        elif operator == "-":
            result = num_1 - num_2
        elif operator == "*":
            result = num_1 * num_2
        elif operator == "/":
            result = num_1 / num_2

        print(f'{num_1} {operator} {num_2} = {result}')

    except ZeroDivisionError:
        print("The developers said you can't divide by zero, sorry.")

math_calculating()

