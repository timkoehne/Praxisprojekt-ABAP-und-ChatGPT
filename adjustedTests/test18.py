

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('', 'x') == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('xyxyxyx', 'x') == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('cacacacac', 'cac') == 4
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('john doe', 'john') == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
