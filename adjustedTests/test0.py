

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
