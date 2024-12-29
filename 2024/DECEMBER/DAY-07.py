#--------------------------------------------------------------------------------------------------
#PART - ONE
#--------------------------------------------------------------------------------------------------
from itertools import product

with open("2024/DEC-INPUTS/DEC-DAY-7.1.txt", 'r') as inputs:

    data = inputs.read().strip().split("\n")

    equations = []
    for line in data:
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        equations.append((test_value, numbers))

    def evaluate(nums, ops):
        result = nums[0]
        for i, op in enumerate(ops):
            if op == "+":
                result += nums[i + 1]
            elif op == "*":
                result *= nums[i + 1]
        return result

    def is_valid_equation(test_value, numbers):
        n = len(numbers) - 1
        for ops in product(["+", "*"], repeat=n):
            if evaluate(numbers, ops) == test_value:
                return True
        return False

    result = 0
    for test_value, numbers in equations:
        if is_valid_equation(test_value, numbers):
            result += test_value

    print("Total:", result)
#--------------------------------------------------------------------------------------------------
#PART - TWO
#--------------------------------------------------------------------------------------------------
from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        elif op == "||":
            result = int(str(result) + str(numbers[i + 1]))
    return result

with open("2024/DEC-INPUTS/DEC-DAY-7.2.txt", 'r') as inputs:
    data = inputs.read().strip().split("\n")
    total_result = 0

    for line in data:
        target, *numbers = line.replace(":", "").split()
        target = int(target)
        numbers = list(map(int, numbers))
        n = len(numbers)

        valid = False
        for operators in product(["+", "*", "||"], repeat=n - 1):
            if evaluate_expression(numbers, operators) == target:
                valid = True
                break

        if valid:
            total_result += target

    print("Total:", total_result)
#--------------------------------------------------------------------------------------------------