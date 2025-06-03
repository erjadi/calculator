"""
Test suite for Calculator - Iteration 2
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
