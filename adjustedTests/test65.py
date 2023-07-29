def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(100, 2) == "001"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(12, 2) == "12"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(97, 8) == "79"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
