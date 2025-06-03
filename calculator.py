"""
Simple Calculator Module - Iteration 6
Addition, subtraction, multiplication, division, power, and square root functionality
"""
import math


class Calculator:
    """A simple calculator class."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers and return the result."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide a by b and return the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        """Raise a to the power of b and return the result."""
        # BUG: Using XOR operator ^ instead of ** for power
        result = a ^ b
        self.history.append(f"{a} ** {b} = {result}")
        return result
    
    def sqrt(self, a):
        """Calculate the square root of a number."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(a)
        self.history.append(f"sqrt({a}) = {result}")
        return result
    
    def get_history(self):
        """Return calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
