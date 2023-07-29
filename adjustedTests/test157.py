def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(3, 4, 5) == True, "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1, 2, 3) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10, 6, 8) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 2, 2) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7, 24, 25) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10, 5, 7) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5, 12, 13) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(15, 8, 17) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(48, 55, 73) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(1, 1, 1) == False, "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 2, 10) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
