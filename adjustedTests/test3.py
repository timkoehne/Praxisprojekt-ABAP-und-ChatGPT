

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, -3, 1, 2, -3]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, -4, 5, 6]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, -1, 2, -2, 5, -5, 4, -4]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, -1, 2, -2, 5, -5, 4, -5]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, -2, 2, -2, 5, -5, 4, -4]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
