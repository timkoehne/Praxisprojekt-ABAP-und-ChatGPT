def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(5, 6, 10) == [11, 4], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4, 8, 9) == [12, 1], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1, 10, 10) == [11, 0], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 11, 5) == [7, 0], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(4, 5, 7) == [9, 2], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4, 5, 1) == [5, 0], "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
