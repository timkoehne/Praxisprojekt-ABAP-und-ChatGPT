def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(14) == [1, 5, 7, 11, 13, 17]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5) == [1, 5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(12) == [1, 3, 5], "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(1) == [1], "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
