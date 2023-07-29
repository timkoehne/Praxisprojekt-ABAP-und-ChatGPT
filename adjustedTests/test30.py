

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([-1, -2, 4, 5, 6]) == [4, 5, 6]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-1, -2]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
