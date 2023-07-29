def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([3, 2, 3], 9) is True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2], 5) is False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3], 5) is True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 2, 3], 1) is False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([1, 2, 3], 6) is False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5], 5) is True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
