# 📘 Assignment: Writing Tests for Python Code

## 🎯 Objective

Learn how to verify your code works correctly using unit tests. You'll write test cases using the pytest framework to catch bugs early, validate function behavior, and build confidence in your code before deployment.

## 📝 Tasks

### 🛠️ Write Your First Unit Tests

#### Description
Create simple test cases for a provided set of functions using pytest assertions.

#### Requirements
Completed program should:

- Install pytest and create a test file following naming convention (`test_*.py`)
- Write at least 3 test functions using `assert` statements
- Test basic function behavior: correct results, edge cases, and expected values
- Run tests using `pytest test_functions.py`
- Verify all tests pass

### 🛠️ Test Edge Cases and Error Handling

#### Description
Expand testing to cover edge cases, boundary conditions, and error scenarios.

#### Requirements
Completed program should:

- Write tests for edge cases (empty inputs, zero, negative numbers, etc.)
- Test that functions raise appropriate exceptions when given invalid input
- Use pytest's `pytest.raises()` context manager to test exception handling
- Organize tests into logical groups using test classes
- Achieve at least 80% code coverage for tested functions

### 🛠️ Build a Test Suite for a Real Function

#### Description
Write a comprehensive test suite for a more complex function, including setup and teardown if needed.

#### Requirements
Completed program should:

- Create multiple test functions covering normal operation and edge cases
- Use `@pytest.fixture` to set up shared test data if needed
- Write parameterized tests using `@pytest.mark.parametrize` to test multiple input scenarios
- Generate a coverage report using pytest-cov
- Document test cases with clear docstrings explaining what each test validates
