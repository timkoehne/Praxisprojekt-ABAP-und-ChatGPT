def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(12, 15) == 14
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(13, 12) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(33, 12354) == 12354
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5234, 5233) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(6, 29) == 28
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(27, 10) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(7, 7) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(546, 546) == 546
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
