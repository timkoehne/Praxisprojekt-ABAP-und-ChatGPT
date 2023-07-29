

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(1) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(6) == 21
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(11) == 66
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(30) == 465
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(100) == 5050
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
