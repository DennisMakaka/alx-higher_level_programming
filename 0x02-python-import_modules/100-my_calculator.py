#!/usr/bin/pyton

if __name__ == "__main__":
    """Handle basic arithmetic operations"""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        """Define the supported operators and check if the provided operator is valid"""
        ops = {"+": add, "-": sub, "*": mul, "/": div}
        operator = sys.argv[2]
        if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sts.exit(1)

        """Extract operands and perform the operation"""
        a,b = int(sys.argv[1]), int(sys.argv[3])
        result = ops[operator](a, b)

        """Print the result"""
        print(f"{a} {operator} {b} = {result}")
