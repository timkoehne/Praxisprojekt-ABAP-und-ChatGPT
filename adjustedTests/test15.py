

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(0) == '0'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3) == '0 1 2 3'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
