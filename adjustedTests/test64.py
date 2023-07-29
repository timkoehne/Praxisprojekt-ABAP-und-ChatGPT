def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("abcde") == 2, "Test 1"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Alone") == 3, "Test 2"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("key") == 2, "Test 3"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("bye") == 1, "Test 4"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("keY") == 2, "Test 5"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("bYe") == 1, "Test 6"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("ACEDY") == 3, "Test 7"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
