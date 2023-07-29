def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([1,2,4,3,5])==3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1,2,4,5])==-1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1,4,2,5,6,7,8,9,10])==2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4,8,5,7,3])==4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([])==-1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
