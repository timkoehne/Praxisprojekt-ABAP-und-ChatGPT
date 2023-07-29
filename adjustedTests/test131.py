def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(5) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(54) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(120) ==1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5014) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(98765) == 315
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5576543) == 2625
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(2468) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
