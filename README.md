# Calculator

A simple Python calculator implementation with basic mathematical operations and calculation history tracking.

## Features

- **Basic Arithmetic Operations**:
  - Addition (`add`)
  - Subtraction (`subtract`)
  - Multiplication (`multiply`)
  - Division (`divide`)
  - Power/Exponentiation (`power`)
  - Square root (`sqrt`)
  - Modulo (`modulo`)

- **Additional Features**:
  - Calculation history tracking
  - History management (view and clear)
  - Error handling for edge cases (division by zero, negative square roots, etc.)

## Project Structure

```
calculator/
├── calculator.py          # Main calculator implementation
├── test_calculator.py     # Comprehensive test suite
├── README.md             # This file
└── TODO.md               # Known issues and future improvements
```

## Usage

```python
from calculator import Calculator

# Create calculator instance
calc = Calculator()

# Perform calculations
result = calc.add(5, 3)        # Returns 8
result = calc.multiply(4, 7)   # Returns 28
result = calc.divide(10, 2)    # Returns 5.0
result = calc.power(2, 3)      # Returns 8
result = calc.sqrt(16)         # Returns 4.0
result = calc.modulo(10, 3)    # Returns 1

# View calculation history
history = calc.get_history()
print(history)

# Clear history
calc.clear_history()
```

## Testing

The project includes a comprehensive test suite using pytest. To run the tests:

```bash
pytest test_calculator.py
```

## Requirements

- Python 3.x
- pytest (for running tests)

## Error Handling

The calculator handles common edge cases:
- Division by zero raises `ValueError`
- Square root of negative numbers raises `ValueError`
- Modulo with zero divisor raises `ValueError`

## Version

Current version: Iteration 7
