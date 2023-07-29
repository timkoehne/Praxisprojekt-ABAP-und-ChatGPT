def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(3) == [3, 5, 7], "Test 3"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4) == [4,6,8,10], "Test 4"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5) == [5, 7, 9, 11, 13]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(6) == [6, 8, 10, 12, 14, 16]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8) == [8, 10, 12, 14, 16, 18, 20, 22]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
