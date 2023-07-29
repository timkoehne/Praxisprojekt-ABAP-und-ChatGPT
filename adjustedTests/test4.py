

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
