def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate('aBCdEf')  == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('abcdefg') == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('dBBE') == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('B')  == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('U')  == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('') == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('EEEE') == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
