def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate((1, 2), (2, 3)) == "NO"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate((-1, 1), (0, 4)) == "NO"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate((-3, -1), (-5, 5)) == "YES"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate((-2, 2), (-4, 0)) == "YES"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate((-11, 2), (-1, -1)) == "NO"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate((1, 2), (3, 5)) == "NO"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate((1, 2), (1, 2)) == "NO"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate((-2, -2), (-3, -2)) == "NO"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
