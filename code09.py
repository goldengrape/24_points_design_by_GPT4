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
