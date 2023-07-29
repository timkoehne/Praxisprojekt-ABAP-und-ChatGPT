

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
