import itertools
import math

def recursive_calculate(expression, steps, target=24, operators=("+", "-", "*", "/")):
    if len(expression) == 1:
        if expression[0] is not None and math.isclose(expression[0], target, rel_tol=1e-9):
            return steps
        else:
            return None

    for i, num in enumerate(expression[:-1]):
        for op in operators:
            result = apply_operator(op, num, expression[i+1])
            if result is None:
                continue
            new_expression = expression[:i] + (result,) + expression[i+2:]
            new_steps = steps + [(op, num, expression[i+1])]
            res_steps = recursive_calculate(new_expression, new_steps, target)
            if res_steps is not None:
                return res_steps
    return None

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
        steps = recursive_calculate(perm, [])
        if steps is not None:
            return steps, perm
    return None, None

def format_expression(perm, steps):
    expression = [str(x) for x in perm]
    for op, a, b in steps:
        a = str(a)
        b = str(b)
        try:
            idx_a = expression.index(a)
            idx_b = expression.index(b, idx_a + 1)
            expression[idx_a:idx_b + 1] = [f"({expression[idx_a]} {op} {expression[idx_b]})"]
        except ValueError:
            pass
    return expression[0]

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

    steps, perm = find_expression(nums)
    if steps is not None:
        print("找到一个可以得到 24 的计算式：")
        expression = format_expression(perm, steps)
        print(f"{expression} = 24")
    else:
        print("无法通过四则运算得到 24。")
