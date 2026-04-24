# Calculator

## Overview
Simple command-line calculator supporting basic arithmetic operations.

## Features
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Exponentiation (^ or **)
- Modulus (%)
- Parentheses for grouping

## Usage
Run the program:
```
python calculator.py
```
Enter an expression when prompted, e.g.:
```
> 2 + 3 * 4
Result: 14
```
Type `exit` or `quit` to stop.

## Functions
- `add(a, b)`: returns a + b
- `subtract(a, b)`: returns a - b
- `multiply(a, b)`: returns a * b
- `divide(a, b)`: returns a / b (raises ZeroDivisionError if b == 0)
- `power(a, b)`: returns a ** b
- `mod(a, b)`: returns a % b

## Example
```
> (10 + 5) * 2
Result: 30
> 7 / 0
Error: division by zero
```