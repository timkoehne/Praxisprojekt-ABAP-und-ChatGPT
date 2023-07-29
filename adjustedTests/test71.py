def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(3, 4, 5) == 6.00, "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1, 2, 10) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4, 8, 5) == 8.18
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 2, 2) == 1.73
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1, 2, 3) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10, 5, 7) == 16.25
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 6, 3) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(1, 1, 1) == 0.43, "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 2, 10) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
