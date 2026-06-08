"""
Starter code for Testing with pytest assignment.
This file contains example functions and basic test cases to get you started.
"""

# ============================================================================
# EXAMPLE FUNCTIONS - These are the functions you'll write tests for
# ============================================================================

def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(number):
    """Return True if number is even, False otherwise."""
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return number % 2 == 0


def reverse_string(text):
    """Reverse a string and return the result."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]


def find_max(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


# ============================================================================
# EXAMPLE TESTS - These show you how to write tests with pytest
# ============================================================================

import pytest


class TestAddFunction:
    """Test cases for the add() function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(0, 0) == 0


class TestDivideFunction:
    """Test cases for the divide() function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError):
            divide(10, 0)


class TestIsEvenFunction:
    """Test cases for the is_even() function."""
    
    def test_even_numbers(self):
        """Test that even numbers return True."""
        assert is_even(2) == True
        assert is_even(0) == True
        assert is_even(-4) == True
    
    def test_odd_numbers(self):
        """Test that odd numbers return False."""
        assert is_even(1) == False
        assert is_even(-3) == False
    
    def test_non_integer_raises_error(self):
        """Test that non-integers raise TypeError."""
        with pytest.raises(TypeError):
            is_even(3.5)
        with pytest.raises(TypeError):
            is_even("5")


# ============================================================================
# YOUR TASK: Write tests for reverse_string() and find_max()
# ============================================================================

# TODO: Create test cases for reverse_string()
# Test normal strings, empty strings, special characters, etc.

# TODO: Create test cases for find_max()
# Test lists with positive/negative numbers, edge cases, and errors


# ============================================================================
# ADVANCED: Parameterized tests example
# ============================================================================

class TestParametrized:
    """Example of using parameterized tests to test multiple scenarios."""
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
    ])
    def test_add_multiple_values(self, a, b, expected):
        """Test add() with multiple input scenarios."""
        assert add(a, b) == expected
