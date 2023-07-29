

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(2) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5) == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8) == 24
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == 81
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(12) == 274
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(14) == 927
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
