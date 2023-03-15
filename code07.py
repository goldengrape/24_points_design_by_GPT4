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
