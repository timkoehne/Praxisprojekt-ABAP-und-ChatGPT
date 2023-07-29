def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([1,2,3,5,4,7,9,6]) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3, 4, 3, 2, 2]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 4, 2]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 4, 4, 2]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([1, 2, 3, 2, 1]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 1, 1, 3]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([0, 1]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
