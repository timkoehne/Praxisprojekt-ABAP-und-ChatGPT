

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([1, 2, 3]) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
