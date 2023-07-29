def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([1, 2, 2, -4]) == -9
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([0, 1]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 1, 1, 2, 3, -1, 1]) == -10
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([]) == None
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 4,1, 2, -1, -1, 9]) == 20
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, 1, -1, 1]) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, 1, 1, 1]) == -4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, 1, 1, 0]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
