def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, -2, 0]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 1, 2, -2, 3, 4, 5]) == 6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 6, 9, -6, 0, 1, 5]) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 100, 98, -7, 1, -1]) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([12, 23, 34, -45, -56, 0]) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-0, 1**0]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
