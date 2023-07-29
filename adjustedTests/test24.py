

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(3) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(100) == 50
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(49) == 7
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
