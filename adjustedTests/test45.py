

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(5, 3) == 7.5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 2) == 2.0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10, 8) == 40.0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
