def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(4) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(6) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(11) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(12) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(13) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(16) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
