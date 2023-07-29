def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([1, 2, 3, 4, 5]) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 1, 4, 3, 2]) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([]) == None
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 1]) == None
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1,1,1,1,0]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 0**0]) == None
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-35, 34, 12, -45]) == -35
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
