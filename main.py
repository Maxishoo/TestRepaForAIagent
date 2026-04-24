<<<FILE: main.py>>>
import ast
import operator as op
import sys

# Supported operators
_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
}

class Evaluator(ast.NodeVisitor):
    """Safe AST evaluator for basic arithmetic."""
    def visit_Expression(self, node):
        return self.visit(node.body)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_type = type(node.op)
        if op_type not in _OPERATORS:
            raise ValueError(f"Unsupported operator {op_type}")
        func = _OPERATORS[op_type]
        # Handle division by zero, modulo zero, floor division by zero
        if op_type in (ast.Div, ast.FloorDiv, ast.Mod) and right == 0:
            raise ZeroDivisionError("division by zero")
        return func(left, right)

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand
        raise ValueError(f"Unsupported unary operator {type(node.op)}")

    def visit_Num(self, node):  # Python <3.8
        return node.n

    def visit_Constant(self, node):  # Python >=3.8
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Constants must be numeric")

    def generic_visit(self, node):
        raise ValueError(f"Unsupported expression: {ast.dump(node)}")

def evaluate(expr: str):
    """Evaluate a mathematical expression safely."""
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError as e:
        raise SyntaxError(f"Invalid expression: {e}") from None
    evaluator = Evaluator()
    return evaluator.visit(tree)

def repl():
    print("Simple Calculator REPL")
    print("Enter an expression to evaluate, or 'exit'/'quit' to stop.")
    print("Supported: +, -, *, /, //, %, **, parentheses, unary +/-")
    while True:
        try:
            expr = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        if not expr:
            continue
        if expr.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        try:
            result = evaluate(expr)
            # Print as integer if result is integral
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
<<<END FILE>>>
<<<FILE: README.md>>>
# Simple Calculator REPL

A small, safe calculator implemented in Python that reads arithmetic expressions from a REPL (Read‑Eval‑Print Loop) and prints the result.

## Features

- Supports binary operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Parentheses for grouping
- Unary plus (`+`) and minus (`-`)
- Error handling for:
  - Invalid syntax
  - Division by zero (including `//` and `%`)
  - Unsupported characters or constructs
- Clean exit via `exit`, `quit`, `Ctrl+D`, or `Ctrl+C`

## Usage

Run the script:

```bash
python main.py
```

Then type expressions at the prompt:

```
calc> 2 + 3 * 4
14
calc> (10 - 3) ** 2
49
calc> -5 + 8
3
calc> 10 / 3
3.3333333333333335
calc> 10 // 3
3
calc> 10 % 3
2
calc> exit
Goodbye!
```

## How It Works

- The input string is parsed into an AST using `ast.parse(mode='eval')`.
- A custom `ast.NodeVisitor` (`Evaluator`) walks the tree and computes the result using only the allowed operators and nodes.
- Any attempt to use disallowed syntax (function calls, attribute access, etc.) raises a `ValueError`.
- Division‑by‑zero checks are performed before applying `/`, `//`, or `%`.

## Requirements

- Python 3.6+ (tested on 3.8–3.12)

## License

This code is placed in the public domain; feel free to modify and reuse it as you wish.