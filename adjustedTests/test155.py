def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(7) == (0, 1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(-78) == (1, 1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3452) == (2, 2)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(346211) == (3, 3)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(-345821) == (3, 3)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(-2) == (1, 0)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(-45347) == (2, 3)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(0) == (1, 0)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.

    return passed, failed
