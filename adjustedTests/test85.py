def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([4, 88]) == 88
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 5, 6, 7, 2, 122]) == 122
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 0, 6, 7]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 4, 6, 8]) == 12
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    
    return passed, failed
