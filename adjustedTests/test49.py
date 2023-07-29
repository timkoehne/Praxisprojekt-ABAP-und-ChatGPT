

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(3, 5) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1101, 101) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(0, 101) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3, 11) == 8
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(100, 101) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(30, 5) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(31, 5) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
