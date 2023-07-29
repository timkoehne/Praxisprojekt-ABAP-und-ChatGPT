

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([], 7) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
