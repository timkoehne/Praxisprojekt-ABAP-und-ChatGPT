

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(50) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(78) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(79) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(100) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(200) == 6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4000) == 192
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10000) == 639
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(100000) == 8026
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
