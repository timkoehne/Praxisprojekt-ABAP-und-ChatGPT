def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(1000) == "1", "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(150) == "110", "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(147) == "1100", "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(333) == "1001", "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(963) == "10010", "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
