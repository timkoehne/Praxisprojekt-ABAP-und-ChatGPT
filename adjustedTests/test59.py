

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(15) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(27) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(63) == 7
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(330) == 11
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(13195) == 29
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
