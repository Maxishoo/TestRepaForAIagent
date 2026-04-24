# Calculator

A simple command‑line calculator implemented in Python. It provides an interactive REPL where you can type arithmetic expressions and see the result instantly.

## Features
- Supports basic arithmetic: `+`, `-`, `*`, `/`
- Integer division `//` and modulus `%`
- Exponentiation `**`
- Parentheses for grouping
- Handles floating‑point and integer numbers
- Clean exit commands and keyboard interrupts

## How to Run
```bash
python main.py
```
The program will start a REPL prompt (`> `). Type your expression and press **Enter** to see the result.

## Usage Examples
```
> 2 + 3 * 4
14
> (1 + 2) * 5
15
> 10 / 3
3.3333333333333335
> 10 // 3
3
> 10 % 3
1
> 2 ** 8
256
```

## Exiting the REPL
- Type `exit` or `quit` and press **Enter**
- Press **Ctrl+D** (EOF) on Linux/macOS or **Ctrl+Z** then **Enter** on Windows
- Press **Ctrl+C** to interrupt and exit

Feel free to extend the calculator with more functions or features as needed!