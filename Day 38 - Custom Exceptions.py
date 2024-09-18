"""
Day 38 - Custom Exceptions
Create a custom exception class.
"""

class CustomException(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f"[Error {self.error_code}]: {self.args[0]}"

def divide(a, b):
    if b == 0:
        raise CustomException("Division by zero is not allowed", 1001)
    return a / b

try:
    result = divide(10, 0)
    print(f"Result: {result}")
except CustomException as e:
    print(e)