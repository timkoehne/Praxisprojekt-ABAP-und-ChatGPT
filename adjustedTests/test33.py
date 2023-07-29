

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert tuple(candidate([1, 2, 3])) == tuple(sort_third([1, 2, 3]))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple(sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple(sort_third([5, 8, -12, 4, 23, 2, 3, 11, 12, -10]))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert tuple(candidate([5, 6, 3, 4, 8, 9, 2])) == tuple([2, 6, 3, 4, 8, 9, 5])
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert tuple(candidate([5, 8, 3, 4, 6, 9, 2])) == tuple([2, 8, 3, 4, 6, 9, 5])
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert tuple(candidate([5, 6, 9, 4, 8, 3, 2])) == tuple([2, 6, 9, 4, 8, 3, 5])
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert tuple(candidate([5, 6, 3, 4, 8, 9, 2, 1])) == tuple([2, 6, 3, 4, 8, 9, 5, 1])
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
