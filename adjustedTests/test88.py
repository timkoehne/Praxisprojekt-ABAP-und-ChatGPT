def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([]) == [], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5]) == [5], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([2, 1]) == [1, 2], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([15, 42, 87, 32 ,11, 0]) == [0, 11, 15, 32, 42, 87], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([21, 14, 23, 11]) == [23, 21, 14, 11], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
