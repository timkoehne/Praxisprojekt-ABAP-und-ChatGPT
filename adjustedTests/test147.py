def check(candidate):
    passed = 0
    failed = 0

    try:
        assert candidate(5) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(6) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == 36
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(100) == 53361
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
