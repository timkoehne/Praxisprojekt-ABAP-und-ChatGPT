def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([]) == [], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, -1 , 55]) == ['One'], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([1, -1, 3, 2]) == ["Three", "Two", "One"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([9, 4, 8]) == ["Nine", "Eight", "Four"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
