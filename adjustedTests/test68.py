def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([4,2,3]) == [2, 1], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1,2,3]) == [2, 1], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([]) == [], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 0, 3, 0, 4, 2]) == [0, 1], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([1, 2, 3, 0, 5, 3]) == [0, 3], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 4, 8, 4 ,8]) == [4, 1], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([7, 6, 7, 1]) == [6, 1], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([7, 9, 7, 1]) == [], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
