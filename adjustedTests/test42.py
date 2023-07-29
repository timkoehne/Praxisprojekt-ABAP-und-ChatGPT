

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([3, 2, 1]) == [4, 3, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
