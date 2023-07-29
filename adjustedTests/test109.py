def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 5, 10, 1, 2])==True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 3, 1, 2])==False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([])==True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
