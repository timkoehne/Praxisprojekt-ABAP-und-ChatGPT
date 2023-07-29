

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
