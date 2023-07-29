def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("10") == 10, "Test 1"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("14.5") == 15, "Test 2"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("-15.5") == -16, "Test 3"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("15.3") == 15, "Test 3"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate("0") == 0, "Test 0"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
