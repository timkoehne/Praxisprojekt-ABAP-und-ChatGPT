def check(candidate):
    passed = 0
    failed = 0

    # manually generated tests
    try:
        assert candidate([5, 5, 5, 5, 1]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 1, 4, 1, 4, 4]) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 3]) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([8, 8, 8, 8, 8, 8, 8, 8]) == 8
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 3, 3, 2, 2]) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # automatically generated tests
    try:
        assert candidate([2, 7, 8, 8, 4, 8, 7, 3, 9, 6, 5, 10, 4, 3, 6, 7, 1, 7, 4, 10, 8, 1]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 2, 8, 2]) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([6, 7, 1, 8, 8, 10, 5, 8, 5, 3, 10]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([8, 8, 3, 6, 5, 6, 4]) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([6, 9, 6, 7, 1, 4, 7, 1, 8, 8, 9, 8, 10, 10, 8, 4, 10, 4, 10, 1, 2, 9, 5, 7, 9]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 9, 10, 1, 3]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([6, 9, 7, 5, 8, 7, 5, 3, 7, 5, 10, 10, 3, 6, 10, 2, 8, 6, 5, 4, 9, 5, 3, 10]) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([8, 8, 10, 6, 4, 3, 5, 8, 2, 4, 2, 8, 4, 6, 10, 4, 2, 1, 10, 2, 1, 1, 5]) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 10, 4, 8, 2, 10, 5, 1, 2, 9, 5, 5, 6, 3, 8, 6, 4, 10]) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 6, 10, 1, 6, 9, 10, 8, 6, 8, 7, 3]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([9, 2, 4, 1, 5, 1, 5, 2, 5, 7, 7, 7, 3, 10, 1, 5, 4, 2, 8, 4, 1, 9, 10, 7, 10, 2, 8, 10, 9, 4]) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 6, 4, 2, 8, 7, 5, 6, 4, 10, 4, 6, 3, 7, 8, 8, 3, 1, 4, 2, 2, 10, 7]) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([9, 8, 6, 10, 2, 6, 10, 2, 7, 8, 10, 3, 8, 2, 6, 2, 3, 1]) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 5, 3, 9, 5, 6, 3, 2, 8, 5, 6, 10, 10, 6, 8, 4, 10, 7, 7, 10, 8]) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([10]) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([9, 7, 7, 2, 4, 7, 2, 10, 9, 7, 5, 7, 2]) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 4, 10, 2, 1, 1, 10, 3, 6, 1, 8]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([7, 9, 9, 9, 3, 4, 1, 5, 9, 1, 2, 1, 1, 10, 7, 5, 6, 7, 6, 7, 7, 6]) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 10, 10, 9, 2]) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
