def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(7, 34, 12) == 34
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(15, 8, 5) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3, 33, 5212) == 33
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1259, 3, 52) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7919, -1, 12) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3609, 1245, 583) == 583
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(91, 56, 129) == 129
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(6, 34, 1234) == 1234
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(1, 2, 0) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 2, 0) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
