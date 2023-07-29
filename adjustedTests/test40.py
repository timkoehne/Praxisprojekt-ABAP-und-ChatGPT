

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([1, 3, 5, 0]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 3, 5, -1]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 3, -2, 1]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3, 7]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 5, 7]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2, 4, -5, 3, 9, 7]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 3, 5, -100]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([100, 3, 5, -100]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
