

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([3, 1, 2, 4, 5]) == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([5]) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([6, 5]) == 5.5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
