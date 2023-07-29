def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(123) == (8, 13)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(12) == (4, 6)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3) == (1, 2)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(63) == (6, 8)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(25) == (5, 6)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(19) == (4, 6)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(9) == (4, 5), "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(1) == (0, 1), "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
