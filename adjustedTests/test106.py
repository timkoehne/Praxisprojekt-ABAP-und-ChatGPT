def check(candidate):
    passed = 0
    failed = 0

    try:
        assert candidate(5) == [1, 2, 6, 24, 15]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1) == [1]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3) == [1, 2, 6]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
