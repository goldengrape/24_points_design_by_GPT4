import itertools
import math

def recursive_calculate(expression, target=24, operators=("+", "-", "*", "/")):
    if len(expression) == 1:
        return math.isclose(expression[0], target, rel_tol=1e-9)

    for i, num in enumerate(expression[:-1]):
        for op in operators:
            new_expression = expression[:i] + (apply_operator(op, num, expression[i+1]),) + expression[i+2:]
            if recursive_calculate(new_expression, target):
                return True
    return False

def apply_operator(operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return None
        return a / b

def find_expression(numbers):
    for perm in itertools.permutations(numbers):
        if recursive_calculate(perm):
            return perm
    return None

if __name__ == "__main__":
    nums = []
    for i in range(4):
        while True:
            num = int(input(f"请输入第 {i + 1} 个 1~10 的整数: "))
            if 1 <= num <= 10:
                break
            else:
                print("输入错误，请输入一个 1~10 的整数。")
        nums.append(num)

    result = find_expression(nums)
    if result is not None:
        print("可以得到 24 的一个数字排列为:", result)
    else:
        print("无法通过四则运算得到 24。")
