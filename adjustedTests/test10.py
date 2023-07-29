

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('') == ''
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('x') == 'x'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('xyz') == 'xyzyx'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('xyx') == 'xyx'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('jerry') == 'jerryrrej'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
