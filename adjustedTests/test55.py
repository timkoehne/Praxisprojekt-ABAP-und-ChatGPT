

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(10) == 55
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8) == 21
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(11) == 89
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(12) == 144
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
