

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(2) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3) == 9
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4) == 16
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8) == 64
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == 100
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
