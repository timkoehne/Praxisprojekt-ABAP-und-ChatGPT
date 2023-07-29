def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(0) == "db0db"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(32) == "db100000db"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(103) == "db1100111db"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(15) == "db1111db", "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
