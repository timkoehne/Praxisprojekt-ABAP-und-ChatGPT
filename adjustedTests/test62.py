

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3]) == [2, 6]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 2, 1]) == [2, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
