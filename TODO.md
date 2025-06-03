# TODO

## Known Issues

### 🐛 Critical Bug - Power Function Implementation
- **Issue**: The `power` function in `calculator.py` uses the XOR operator (`^`) instead of the exponentiation operator (`**`)
- **Location**: Line 42 in `calculator.py`
- **Current code**: `result = a ^ b`
- **Should be**: `result = a ** b`
- **Impact**: Power calculations return incorrect results (bitwise XOR instead of mathematical exponentiation)
- **Priority**: HIGH
- **Status**: Not fixed

#### 🔍 Using Git Bisect to Find the Offending Commit
To identify when this bug was introduced, you can use git bisect:

1. **Start the bisect process**:
   ```bash
   git bisect start
   ```

2. **Mark the current commit as bad** (contains the bug):
   ```bash
   git bisect bad HEAD
   ```

3. **Mark a known good commit** (when power function worked correctly):
   ```bash
   git bisect good <commit-hash>
   # Example: git bisect good v1.0.0
   # Or if you know a specific commit: git bisect good abc123f
   ```

4. **Test each commit that git bisect checks out**:
   - Run the power function test: `python -c "from calculator import Calculator; c = Calculator(); print(c.power(2, 3))"`
   - Expected result: `8` (good), Actual buggy result: `1` (bad)
   - Mark the commit accordingly:
     ```bash
     git bisect good    # if power(2,3) returns 8
     git bisect bad     # if power(2,3) returns 1
     ```

5. **Repeat step 4** until git bisect identifies the exact commit

6. **End the bisect session**:
   ```bash
   git bisect reset
   ```

**Alternative automated approach**:
Create a test script `test_power_bug.py`:
```python
from calculator import Calculator
import sys
calc = Calculator()
result = calc.power(2, 3)
sys.exit(0 if result == 8 else 1)
```

Then run:
```bash
git bisect run python test_power_bug.py
```

## Future Improvements

### 📈 Enhancements
- [ ] Add more advanced mathematical functions (trigonometric, logarithmic)
- [ ] Implement memory functions (store, recall, clear memory)
- [ ] Add support for complex numbers
- [ ] Create a command-line interface (CLI)
- [ ] Add a graphical user interface (GUI)
- [ ] Implement calculation result formatting options
- [ ] Add support for mathematical expressions parsing
- [ ] Implement undo/redo functionality for calculations

### 🧪 Testing
- [ ] Add performance tests for large number calculations
- [ ] Add edge case tests for floating-point precision
- [ ] Add integration tests for history functionality
- [ ] Improve test coverage analysis

### 📚 Documentation
- [ ] Add docstring examples for all methods
- [ ] Create API documentation
- [ ] Add usage examples for all features
- [ ] Create troubleshooting guide

### 🔧 Code Quality
- [ ] Add type hints throughout the codebase
- [ ] Implement logging for debugging
- [ ] Add configuration file support
- [ ] Refactor for better separation of concerns
- [ ] Add input validation decorators

### 🚀 Performance
- [ ] Optimize calculations for large numbers
- [ ] Add caching for expensive operations
- [ ] Implement lazy evaluation for chained operations

## Completed Items

- ✅ Basic arithmetic operations implementation
- ✅ Error handling for division by zero
- ✅ Error handling for negative square roots
- ✅ Calculation history tracking
- ✅ Comprehensive test suite
- ✅ History management functions
