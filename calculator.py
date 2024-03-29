# -*- coding: utf-8 -*-
"""calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sF99bo9AWd8RzvHC14eEtetYj-n1D8Wf
"""



class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot be divided by zero"

operation = input("Enter the operation in the format 'number1 operator number2' (e.g., 1 + 2): ")

operands = operation.split()
x = float(operands[0])
y = float(operands[2])
op = operands[1]

result = None
if op == '+':
    result = Calculator.add(x, y)
elif op == '-':
    result = Calculator.sub(x, y)
elif op == '*':
    result = Calculator.mul(x, y)
elif op == '/':
    result = Calculator.div(x, y)
else:
    print("Invalid operator")

if result is not None:
    print(f"The result of {operation} is {result}")