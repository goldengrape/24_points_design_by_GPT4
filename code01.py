import itertools
import math

def calculate_24(numbers):
    def op(a, b, operator):
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

    operators = ["+", "-", "*", "/"]
    possible_combinations = list(itertools.permutations(numbers))

    for numbers in possible_combinations:
        for op1 in operators:
            for op2 in operators:
                for op3 in operators:
                    # 先算第一个操作符，再算第二个，最后算第三个
                    a = op(op(numbers[0], numbers[1], op1), op(numbers[2], numbers[3], op3), op2)
                    if a is not None and math.isclose(a, 24, rel_tol=1e-9):
                        return f"(({numbers[0]} {op1} {numbers[1]}) {op2} ({numbers[2]} {op3} {numbers[3]}))"

                    # 先算前两个操作符，再算第三个
                    b = op(op(numbers[0], numbers[1], op1), numbers[2], op2)
                    if b is not None:
                        b = op(b, numbers[3], op3)
                        if math.isclose(b, 24, rel_tol=1e-9):
                            return f"(({numbers[0]} {op1} {numbers[1]} {op2} {numbers[2]}) {op3} {numbers[3]})"

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

    result = calculate_24(nums)
    if result is not None:
        print("可以得到 24 的计算式为:", result)
    else:
        print("无法通过四则运算得到 24。")
