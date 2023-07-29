

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(1) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4) == 13
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5) == 89
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(6) == 233
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7) == 1597
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8) == 28657
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(9) == 514229
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == 433494437
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
