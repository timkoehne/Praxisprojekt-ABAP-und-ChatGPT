

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 3, 2, 8], []) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
