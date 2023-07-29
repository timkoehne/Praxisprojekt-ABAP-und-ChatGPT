

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(8, 3) == "22"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(9, 3) == "100"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(234, 2) == "11101010"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(16, 2) == "10000"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8, 2) == "1000"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7, 2) == "111"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    for x in range(2, 8):
        try:
            assert candidate(x, x + 1) == str(x)
            passed += 1
        except (AssertionError, TypeError):
            failed += 1

    return passed, failed
