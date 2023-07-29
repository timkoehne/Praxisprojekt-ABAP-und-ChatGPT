def check(candidate):
    passed = 0
    failed = 0


    # Check some simple cases
    try:
        assert candidate([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[0,0,0], [0,0,0]], 5) == 0, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([[1,1,1,1], [1,1,1,1]], 2) == 4, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[1,1,1,1], [1,1,1,1]], 9) == 2, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
