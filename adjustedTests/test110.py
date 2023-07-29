def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3, 4], [2, 1, 4, 3]) == "YES" 
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 7, 3], [2, 6, 4]) == "YES"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 7, 3], [2, 6, 3]) == "NO" 
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([100, 200], [200, 200]) == "YES"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
