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
            new_steps = steps + [(op, num, expression[i+1], result)]
            res_steps = recursive_calculate(new_expression, new_steps, target)
            if res_steps is not None:
                return res_steps
    return None

def format_expression(steps):
    expression = {}
    for step in steps:
        op, a, b, res = step
        expression[res] = f"({expression.get(a, a)} {op} {expression.get(b, b)})"
    return expression[res]

# ... (保留其他代码不变)

if __name__ == "__main__":
    # ... (保留输入代码不变)
    
    steps, perm = find_expression(nums)
    if steps is not None:
        print("找到一个可以得到 24 的计算式：")
        expression = format_expression(steps)
        print(f"{expression} = 24")
    else:
        print("无法通过四则运算得到 24。")
