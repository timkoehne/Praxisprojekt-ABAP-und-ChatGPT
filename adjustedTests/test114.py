def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([2, 3, 4, 1, 2, 4]) == 1, "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, -2, -3]) == -6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, -2, -3, 2, -10]) == -14
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-9999999999999999]) == -9999999999999999
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([0, 10, 20, 1000000]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, -2, -3, 10, -5]) == -6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([100, -1, -2, -3, 10, -5]) == -6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([10, 11, 13, 8, 3, 4]) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([100, -33, 32, -1, 0, -2]) == -33
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([-10]) == -10, "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([7]) == 7
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, -1]) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
