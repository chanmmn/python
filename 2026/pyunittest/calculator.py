"""A simple calculator module for demonstration."""


class Calculator:
    """A basic calculator class with arithmetic operations."""
    
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b
    
    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b
    
    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b
    
    def divide(self, a, b):
        """Return the quotient of a and b.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Return base raised to the power of exponent."""
        return base ** exponent
