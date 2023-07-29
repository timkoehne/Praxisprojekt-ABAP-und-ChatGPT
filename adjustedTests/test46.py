

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(5) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8) == 28
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == 104
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(12) == 386
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
