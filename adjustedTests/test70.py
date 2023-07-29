def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 6, 7, 8, 9, 1]) == [1, 9, 5, 8, 6, 7]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 5, 5, 5]) == [5, 5, 5, 5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1,2,3,4,5,6,7,8]) == [1, 8, 2, 7, 3, 6, 4, 5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([0,2,2,2,5,5,-5,-5]) == [-5, 5, -5, 5, 0, 2, 2, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([111111]) == [111111]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
