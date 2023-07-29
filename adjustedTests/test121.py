def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([5, 8, 7, 1])    == 12
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 3, 3, 3, 3]) == 9
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([30, 13, 24, 321]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 9]) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 4, 8]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([30, 13, 23, 32]) == 23
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 13, 2, 9]) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
