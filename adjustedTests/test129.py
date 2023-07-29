def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    print
    try:
        assert candidate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [1, 2, 1]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == [1]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4) == [1, 2, 1, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[6, 4, 13, 10], [5, 7, 12, 1], [3, 16, 11, 15], [8, 14, 9, 2]], 7) == [1, 10, 1, 10, 1, 10, 1]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[8, 14, 9, 2], [6, 4, 13, 15], [5, 7, 1, 12], [3, 10, 11, 16]], 5) == [1, 7, 1, 7, 1]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[11, 8, 7, 2], [5, 16, 14, 4], [9, 3, 15, 6], [12, 13, 10, 1]], 9) == [1, 6, 1, 6, 1, 6, 1, 6, 1]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[12, 13, 10, 1], [9, 3, 15, 6], [5, 16, 14, 4], [11, 8, 7, 2]], 12) == [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[2, 7, 4], [3, 1, 5], [6, 8, 9]], 8) == [1, 3, 1, 3, 1, 3, 1, 3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[6, 1, 5], [3, 8, 9], [2, 7, 4]], 8) == [1, 5, 1, 5, 1, 5, 1, 5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([[1, 2], [3, 4]], 10) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([[1, 3], [3, 2]], 10) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
