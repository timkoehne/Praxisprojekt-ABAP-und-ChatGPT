

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(2) == [2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4) == [2, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(8) == [2, 2, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3 * 19) == [3, 19]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3 * 19 * 3 * 19) == [3, 3, 19, 19]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3 * 19 * 19 * 19) == [3, 19, 19, 19]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(3 * 2 * 3) == [2, 3, 3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
