import math

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def safe_factorial(n):
    if n < 0 or not n.is_integer():
        return "Undefined (factorial defined for non-negative integers only)"
    try:
        return math.factorial(int(n))
    except (ValueError, OverflowError):
        return "Overflow or invalid input"

def main():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")

    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print(f"{a} / {b} = Division by zero")

    print(f"{a} ^ {b} = {a ** b}")

    if b != 0:
        print(f"{a} % {b} = {a % b}")
    else:
        print(f"{a} % {b} = Modulus by zero")

    print(f"factorial({a}) = {safe_factorial(a)}")
    print(f"factorial({b}) = {safe_factorial(b)}")

    print(f"sin({a}) = {math.sin(a)}")
    print(f"cos({a}) = {math.cos(a)}")
    if math.cos(a) != 0:
        print(f"tan({a}) = {math.tan(a)}")
    else:
        print(f"tan({a}) = Undefined (cosine is zero)")

if __name__ == "__main__":
    main()