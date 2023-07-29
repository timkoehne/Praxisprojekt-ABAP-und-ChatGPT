

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(6) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(101) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(11) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(13441) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(61) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(11) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(17) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5 * 17) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(11 * 7) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(13441 * 19) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
