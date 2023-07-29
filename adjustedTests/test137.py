def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(1, 2) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1, 2.5) == 2.5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 3) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5, 6) == 6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1, "2,3") == "2,3"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("5,1", "6") == "6"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1", "2") == "2"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1", 1) == None
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
