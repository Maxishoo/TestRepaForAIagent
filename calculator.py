def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b!=0 else None

def main():
    while True:
        try:
            a=float(input("Enter first number: "))
            op=input("Enter operator (+,-,*,/): ")
            b=float(input("Enter second number: "))
            if op=='+': print(add(a,b))
            elif op=='-': print(sub(a,b))
            elif op=='*': print(mul(a,b))
            elif op=='/':
                if b==0: print("Error: division by zero")
                else: print(div(a,b))
            else: print("Invalid operator")
        except ValueError:
            print("Invalid input")
        cont=input("Continue? (y/n): ")
        if cont.lower()!='y': break

if __name__=="__main__":
    main()