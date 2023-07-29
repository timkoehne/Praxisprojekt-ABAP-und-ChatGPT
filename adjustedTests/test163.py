def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(2, 10) == [2, 4, 6, 8], "Test 1"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10, 2) == [2, 4, 6, 8], "Test 2"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(132, 2) == [2, 4, 6, 8], "Test 3"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(17,89) == [], "Test 4"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
