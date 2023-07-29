def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(4) == 288, "Test 4"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5) == 34560, "Test 5"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7) == 125411328000, "Test 7"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(1) == 1, "Test 1"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
