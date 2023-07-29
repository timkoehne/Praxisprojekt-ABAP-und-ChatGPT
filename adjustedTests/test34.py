

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
