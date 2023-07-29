

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([2.0, 49.9]) == [0.0, 1.0]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([100.0, 49.9]) == [1.0, 0.0]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
