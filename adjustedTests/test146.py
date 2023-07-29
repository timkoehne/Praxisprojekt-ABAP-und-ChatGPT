def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([5, -2, 1, -5]) == 0  
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([15, -73, 14, -15]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([33, -2, -3, 45, 21, 109]) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([43, -12, 93, 125, 121, 109]) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([71, -2, -33, 75, 21, 19]) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([1]) == 0              
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([]) == 0                   
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
