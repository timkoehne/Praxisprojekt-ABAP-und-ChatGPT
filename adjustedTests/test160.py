def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
