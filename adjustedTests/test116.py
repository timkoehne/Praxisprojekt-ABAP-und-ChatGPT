def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([1,5,2,3,4]) == [1, 2, 4, 3, 5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-2,-3,-4,-5,-6]) == [-4, -2, -6, -5, -3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1,0,2,3,4]) == [0, 1, 2, 4, 3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2,5,77,4,5,3,5,7,2,3,4]) == [2, 2, 4, 4, 3, 3, 5, 5, 5, 7, 77]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3,6,44,12,32,5]) == [32, 3, 5, 6, 12, 44]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2,4,8,16,32]) == [2, 4, 8, 16, 32]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2,4,8,16,32]) == [2, 4, 8, 16, 32]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
