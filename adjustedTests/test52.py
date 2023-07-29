

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([1, 2, 4, 10], 100)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert not candidate([1, 20, 4, 10], 5)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 20, 4, 10], 21)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 20, 4, 10], 22)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 8, 4, 10], 11)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert not candidate([1, 8, 4, 10], 10)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
