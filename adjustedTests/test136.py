def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([2, 4, 1, 3, 5, 7]) == (None, 1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 4, 1, 3, 5, 7, 0]) == (None, 1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 3, 2, 4, 5, 6, -2]) == (-2, 1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 5, 3, 6, 2, 7, -7]) == (-7, 2)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([7, 3, 8, 4, 9, 2, 5, -9]) == (-9, 2)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([]) == (None, None)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([0]) == (None, None)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, -3, -5, -6]) == (-1, None)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, -3, -5, -6, 0]) == (-1, None)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-6, -4, -4, -3, 1]) == (-3, 1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-6, -4, -4, -3, -100, 1]) == (-3, 1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    return passed, failed
