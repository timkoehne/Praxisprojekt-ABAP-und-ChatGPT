

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([]) == (0, 1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 1, 1]) == (3, 1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([100, 0]) == (100, 0)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([10]) == (10, 10)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
