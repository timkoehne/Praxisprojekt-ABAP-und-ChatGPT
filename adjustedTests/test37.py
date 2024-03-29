

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert tuple(candidate([1, 2, 3])) == tuple([1, 2, 3])
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123])
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10])
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
