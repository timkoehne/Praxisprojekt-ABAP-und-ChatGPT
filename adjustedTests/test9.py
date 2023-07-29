

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
        assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
