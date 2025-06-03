"""
Test suite for Calculator - Iteration 3
"""
import pytest
from calculator import Calculator


class TestCalculator:
    """Test cases for Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = self.calc.add(2, 3)
        assert result == 5
    
    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        result = self.calc.add(-2, -3)
        assert result == -5
    
    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers."""
        result = self.calc.add(5, -3)
        assert result == 2
    
    def test_add_zero(self):
        """Test addition with zero."""
        result = self.calc.add(0, 5)
        assert result == 5
        result = self.calc.add(5, 0)
        assert result == 5
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        result = self.calc.subtract(5, 3)
        assert result == 2
    
    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers."""
        result = self.calc.subtract(-2, -3)
        assert result == 1
    
    def test_subtract_mixed_numbers(self):
        """Test subtraction with mixed positive and negative numbers."""
        result = self.calc.subtract(5, -3)
        assert result == 8
    
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        result = self.calc.subtract(5, 0)
        assert result == 5
        result = self.calc.subtract(0, 5)
        assert result == -5
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        result = self.calc.multiply(4, 3)
        assert result == 12
    
    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        result = self.calc.multiply(-2, -3)
        assert result == 6
    
    def test_multiply_mixed_numbers(self):
        """Test multiplication with mixed positive and negative numbers."""
        result = self.calc.multiply(5, -3)
        assert result == -15
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = self.calc.multiply(5, 0)
        assert result == 0
        result = self.calc.multiply(0, 5)
        assert result == 0
    
    def test_multiply_by_one(self):
        """Test multiplication by one."""
        result = self.calc.multiply(7, 1)
        assert result == 7
        result = self.calc.multiply(1, 7)
        assert result == 7
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        result = self.calc.divide(12, 3)
        assert result == 4
    
    def test_divide_negative_numbers(self):
        """Test division of negative numbers."""
        result = self.calc.divide(-12, -3)
        assert result == 4
    
    def test_divide_mixed_numbers(self):
        """Test division with mixed positive and negative numbers."""
        result = self.calc.divide(-12, 3)
        assert result == -4
    
    def test_divide_by_one(self):
        """Test division by one."""
        result = self.calc.divide(7, 1)
        assert result == 7
    
    def test_divide_zero_by_number(self):
        """Test division of zero by a number."""
        result = self.calc.divide(0, 5)
        assert result == 0
    
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
    
    def test_divide_decimal_result(self):
        """Test division that results in decimal."""
        result = self.calc.divide(7, 2)
        assert result == 3.5
    
    def test_power_positive_numbers(self):
        """Test power operation with positive numbers."""
        result = self.calc.power(2, 3)
        assert result == 8
    
    def test_power_zero_exponent(self):
        """Test power operation with zero exponent."""
        result = self.calc.power(5, 0)
        assert result == 1
    
    def test_power_one_exponent(self):
        """Test power operation with exponent of one."""
        result = self.calc.power(7, 1)
        assert result == 7
    
    def test_power_negative_base(self):
        """Test power operation with negative base."""
        result = self.calc.power(-2, 3)
        assert result == -8
    
    def test_power_negative_exponent(self):
        """Test power operation with negative exponent."""
        result = self.calc.power(2, -2)
        assert result == 0.25
    
    def test_sqrt_positive_number(self):
        """Test square root of positive number."""
        result = self.calc.sqrt(9)
        assert result == 3
    
    def test_sqrt_zero(self):
        """Test square root of zero."""
        result = self.calc.sqrt(0)
        assert result == 0
    
    def test_sqrt_decimal(self):
        """Test square root of decimal number."""
        result = self.calc.sqrt(2.25)
        assert result == 1.5
    
    def test_sqrt_negative_raises_error(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.sqrt(-4)
    
    def test_sqrt_perfect_square(self):
        """Test square root of perfect squares."""
        result = self.calc.sqrt(16)
        assert result == 4
        result = self.calc.sqrt(25)
        assert result == 5
    
    def test_history_tracking(self):
        """Test that calculations are tracked in history."""
        self.calc.add(2, 3)
        self.calc.add(4, 1)
        history = self.calc.get_history()
        assert len(history) == 2
        assert "2 + 3 = 5" in history
        assert "4 + 1 = 5" in history
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(1, 1)
        assert len(self.calc.get_history()) == 1
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0
