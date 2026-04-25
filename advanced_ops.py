import math

def add(a,b):return a+b
def subtract(a,b):return a-b
def multiply(a,b):return a*b
def divide(a,b):return a/b if b!=0 else float('inf')
def power(a,b):return a**b
def sqrt(a):return math.sqrt(a) if a>=0 else float('nan')
def factorial(a):return math.factorial(int(a)) if a>=0 and a==int(a) else float('nan')
def log(a):return math.log(a) if a>0 else float('nan')
def log10(a):return math.log10(a) if a>0 else float('nan')
def sin(a):return math.sin(a)
def cos(a):return math.cos(a)
def tan(a):return math.tan(a)
def asin(a):return math.asin(a) if -1<=a<=1 else float('nan')
def acos(a):return math.acos(a) if -1<=a<=1 else float('nan')
def atan(a):return math.atan(a)
def sinh(a):return math.sinh(a)
def cosh(a):return math.cosh(a)
def tanh(a):return math.tanh(a)