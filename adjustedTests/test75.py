def check(candidate):
    passed = 0
    failed = 0

    try:
        assert candidate(5) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(30) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(125) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3 * 5 * 7) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3 * 6 * 7) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(9 * 9 * 9) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(11 * 9 * 9) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(11 * 13 * 7) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
