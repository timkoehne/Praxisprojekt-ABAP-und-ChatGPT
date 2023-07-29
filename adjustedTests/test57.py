

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([1, 2, 4, 10]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 4, 20]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 20, 4, 10]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 1, 0, -10]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([4, 1, 1, 0]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3, 2, 5, 60]) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 2, 3, 4, 5, 60]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([9, 9, 9, 9]) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
