def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([-3, -4, 5], 3) == [-4, -3, 5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, -4, 4], 2) == [4, 4]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([123, -123, 20, 0 , 1, 2, -3], 3) == [2, 20, 123]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-123, 20, 0 , 1, 2, -3], 4) == [0, 1, 2, 20]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 15, 0, 3, -13, -8, 0], 7) == [-13, -8, 0, 0, 3, 5, 15]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, 0, 2, 5, 3, -10], 2) == [3, 5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 0, 5, -7], 1) == [5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, -4], 2) == [-4, 4]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-10, 10], 2) == [-10, 10]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([1, 2, 3, -23, 243, -400, 0], 0) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
