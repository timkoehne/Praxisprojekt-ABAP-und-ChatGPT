def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(1) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2) == 18
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3) == 180
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4) == 1800
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5) == 18000
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
